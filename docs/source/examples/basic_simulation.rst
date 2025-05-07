Basic Simulation
===============

This example demonstrates a basic Ising model simulation.

Code
----

.. code-block:: python

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

Output
------

The simulation will display:
- A real-time visualization of the spin configuration
- Energy and magnetization plots
- Thermodynamic quantities

.. image:: _static/basic_simulation.png
   :alt: Basic simulation output
   :align: center

Analysis
--------

The simulation shows:
1. Energy relaxation to equilibrium
2. Magnetization fluctuations
3. Phase transition behavior at critical temperature 