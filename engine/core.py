"""Core simulation engine for the Ising model."""

import numpy as np
from dataclasses import dataclass
from typing import Tuple, Optional, List, Dict, Any, Callable
from numba import jit, prange

from utils.logger import setup_logger
from .enums import BoundaryCondition, UpdateRule
from .state_manager import StateManager

class ThermoSimulator:
    """Main simulator class for thermodynamic computing."""
    
    def __init__(
        self,
        grid_size: int = 50,
        temperature: float = 1.0,
        boundary: BoundaryCondition = BoundaryCondition.PERIODIC,
        update_rule: UpdateRule = UpdateRule.METROPOLIS,
        fixed_boundary_value: int = 1,
        mixed_boundary_config: Optional[Dict[str, BoundaryCondition]] = None,
        num_processes: int = 1,
        use_acceleration: bool = True,
        log_level: int = 20  # logging.INFO
    ):
        """Initialize the simulator."""
        self.grid_size = grid_size
        self.temperature = temperature
        self.boundary = boundary
        self.update_rule = update_rule
        self.fixed_boundary_value = fixed_boundary_value
        self.mixed_boundary_config = mixed_boundary_config
        self.num_processes = num_processes
        self.use_acceleration = use_acceleration
        
        # Setup components
        self.logger = setup_logger(log_level)
        from .thermodynamics import SimulationMetrics
        self.metrics = SimulationMetrics()
        self.state_manager = StateManager()
        
        # Initialize grid and metrics
        self._initialize_grid()
        self._initialize_metrics()
        
    def _initialize_grid(self):
        """Initialize the simulation grid."""
        self.grid = np.random.choice([-1, 1], size=(self.grid_size, self.grid_size))
        if self.boundary == BoundaryCondition.FIXED:
            self.grid[0, :] = self.fixed_boundary_value
            self.grid[-1, :] = self.fixed_boundary_value
            self.grid[:, 0] = self.fixed_boundary_value
            self.grid[:, -1] = self.fixed_boundary_value
            
    def _initialize_metrics(self):
        """Initialize simulation metrics."""
        self.energy = self._compute_energy_numba(self.grid)
        self.magnetization = np.sum(self.grid)
        self.accepted_moves = 0
        self.total_moves = 0
        
    @staticmethod
    @jit(nopython=True, parallel=True)
    def _compute_energy_numba(grid: np.ndarray) -> float:
        """Numba-accelerated energy computation."""
        energy = 0.0
        size = grid.shape[0]
        for i in prange(size):
            for j in range(size):
                right = grid[i, (j + 1) % size]
                down = grid[(i + 1) % size, j]
                energy -= grid[i, j] * (right + down)
        return energy / 2
        
    @staticmethod
    @jit(nopython=True)
    def _update_metropolis_numba(grid: np.ndarray, temperature: float) -> Tuple[bool, float]:
        """Numba-accelerated Metropolis update."""
        size = grid.shape[0]
        i, j = np.random.randint(0, size, 2)
        current_spin = grid[i, j]
        
        right = grid[i, (j + 1) % size]
        left = grid[i, (j - 1) % size]
        down = grid[(i + 1) % size, j]
        up = grid[(i - 1) % size, j]
        
        delta_energy = 2 * current_spin * (right + left + down + up)
        
        if delta_energy <= 0 or np.random.random() < np.exp(-delta_energy / temperature):
            grid[i, j] *= -1
            return True, delta_energy
        return False, 0.0
        
    def _update_step(self) -> None:
        """Perform one update step using the selected update rule."""
        if self.use_acceleration:
            if self.update_rule == UpdateRule.METROPOLIS:
                accepted, delta_energy = self._update_metropolis_numba(self.grid, self.temperature)
                if accepted:
                    self.energy += delta_energy
                    self.magnetization += delta_energy  # Delta energy is proportional to magnetization change
                    self.accepted_moves += 1
                self.total_moves += 1
        else:
            # Use non-accelerated methods
            i, j = np.random.randint(0, self.grid_size, 2)
            if self.boundary == BoundaryCondition.FIXED and (i == 0 or i == self.grid_size - 1 or 
                                                           j == 0 or j == self.grid_size - 1):
                return
            
            accepted = False
            if self.update_rule == UpdateRule.METROPOLIS:
                accepted = self._update_metropolis(i, j)
            elif self.update_rule == UpdateRule.GLAUBER:
                accepted = self._update_glauber(i, j)
            elif self.update_rule == UpdateRule.HEAT_BATH:
                accepted = self._update_heat_bath(i, j)
            
            self.total_moves += 1
            if accepted:
                self.accepted_moves += 1
                
    def run(
        self,
        steps: int = 1000,
        plot_interval: int = 100,
        temperature_schedule: Optional[Callable[[int], float]] = None
    ) -> None:
        """Run the simulation."""
        from viz.plotter import Plotter
        plotter = Plotter(self)
        
        for step in range(steps):
            if temperature_schedule is not None:
                self.temperature = temperature_schedule(step)
            
            self._update_step()
            
            if step % plot_interval == 0:
                self.metrics.update(self)
                plotter.update()
                
    def save_state(self, filename: str, format: str = 'h5'):
        """Save simulation state."""
        self.state_manager.save(self, filename, format)
        
    def load_state(self, filename: str, format: str = 'h5'):
        """Load simulation state."""
        self.state_manager.load(self, filename, format) 