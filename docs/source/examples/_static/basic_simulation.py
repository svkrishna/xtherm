"""Generate basic simulation example image."""

import numpy as np
import matplotlib.pyplot as plt
from engine.core import ThermoSimulator
from engine.enums import BoundaryCondition, UpdateRule

# Initialize simulator
simulator = ThermoSimulator(
    grid_size=50,
    temperature=1.0,
    boundary=BoundaryCondition.PERIODIC,
    update_rule=UpdateRule.METROPOLIS
)

# Run simulation
simulator.run(steps=1000, plot_interval=100)

# Save figure
plt.savefig('basic_simulation.png', dpi=300, bbox_inches='tight')
plt.close() 