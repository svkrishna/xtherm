"""Visualization module for the simulation."""

import numpy as np
import matplotlib.pyplot as plt
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.core import ThermoSimulator

class Plotter:
    """Handles visualization of simulation results."""
    
    def __init__(self, simulator: 'ThermoSimulator'):
        """Initialize the plotter."""
        self.simulator = simulator
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(12, 5))
        self.setup_plots()
        
    def setup_plots(self) -> None:
        """Setup the initial plots."""
        # Grid state plot
        self.ax1.set_title('Spin Configuration')
        self.im = self.ax1.imshow(self.simulator.grid, cmap='RdBu')
        plt.colorbar(self.im, ax=self.ax1)
        
        # Energy and magnetization plot
        self.ax2.set_title('Thermodynamic Quantities')
        self.energy_line, = self.ax2.plot([], [], label='Energy')
        self.mag_line, = self.ax2.plot([], [], label='Magnetization')
        self.ax2.legend()
        self.ax2.set_xlabel('Step')
        self.ax2.set_ylabel('Value')
        
        plt.tight_layout()
        
    def update(self) -> None:
        """Update the plots with current simulation state."""
        self._plot_grid_state()
        self._plot_energy_magnetization()
        plt.pause(0.001)
        
    def _plot_grid_state(self) -> None:
        """Update the grid state plot."""
        self.im.set_array(self.simulator.grid)
        
    def _plot_energy_magnetization(self) -> None:
        """Update the energy and magnetization plot."""
        steps = range(len(self.simulator.metrics.energy_history))
        self.energy_line.set_data(steps, self.simulator.metrics.energy_history)
        self.mag_line.set_data(steps, self.simulator.metrics.magnetization_history)
        
        # Update axis limits
        self.ax2.relim()
        self.ax2.autoscale_view()
        
    def close(self):
        """Close the plotter and its figure."""
        plt.close(self.fig) 