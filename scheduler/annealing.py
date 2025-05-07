"""Temperature annealing schedules for the simulation."""

import numpy as np

def boltzmann_annealing(initial_temp: float, step: int, decay_rate: float = 0.95) -> float:
    """Boltzmann annealing schedule: T(t) = T₀ * exp(-αt)."""
    return initial_temp * np.exp(-decay_rate * step)

def cauchy_annealing(initial_temp: float, step: int, decay_rate: float = 0.1) -> float:
    """Cauchy annealing schedule: T(t) = T₀ / (1 + αt)."""
    return initial_temp / (1 + decay_rate * step)

def adaptive_annealing(initial_temp: float, step: int, acceptance_rate: float) -> float:
    """Adaptive annealing based on acceptance rate."""
    if acceptance_rate > 0.5:
        return initial_temp * 0.95
    return initial_temp * 1.05 