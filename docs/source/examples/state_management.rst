State Management
===============

This example demonstrates saving and loading simulation states.

Code
----

.. code-block:: python

    import numpy as np
    from engine.core import ThermoSimulator
    from engine.enums import BoundaryCondition, UpdateRule

    # Initialize simulator
    simulator = ThermoSimulator(
        grid_size=50,
        temperature=2.27,
        boundary=BoundaryCondition.PERIODIC,
        update_rule=UpdateRule.METROPOLIS
    )

    # Run simulation for some steps
    simulator.run(steps=500)

    # Save state
    simulator.save_state('simulation_state.h5')

    # Create new simulator
    new_simulator = ThermoSimulator(
        grid_size=50,
        temperature=2.27,
        boundary=BoundaryCondition.PERIODIC,
        update_rule=UpdateRule.METROPOLIS
    )

    # Load state
    new_simulator.load_state('simulation_state.h5')

    # Verify state
    print(f"Original energy: {simulator.energy}")
    print(f"Loaded energy: {new_simulator.energy}")
    print(f"Original magnetization: {simulator.magnetization}")
    print(f"Loaded magnetization: {new_simulator.magnetization}")

Output
------

.. code-block:: text

    Original energy: -4832.0
    Loaded energy: -4832.0
    Original magnetization: 156
    Loaded magnetization: 156

Analysis
--------

The state management features:
1. Save complete simulation state to HDF5 format
2. Load state into new simulator instance
3. Verify state consistency through thermodynamic quantities 