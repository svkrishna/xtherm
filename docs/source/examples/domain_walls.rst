Domain Walls
============

This example demonstrates domain wall formation and dynamics.

Code
----

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt
    from engine.core import ThermoSimulator
    from engine.enums import BoundaryCondition, UpdateRule

    # Initialize simulator with mixed boundaries
    mixed_config = {
        'left': BoundaryCondition.FIXED,
        'right': BoundaryCondition.FIXED,
        'top': BoundaryCondition.PERIODIC,
        'bottom': BoundaryCondition.PERIODIC
    }

    simulator = ThermoSimulator(
        grid_size=50,
        temperature=1.5,
        boundary=BoundaryCondition.MIXED,
        mixed_boundary_config=mixed_config,
        update_rule=UpdateRule.METROPOLIS
    )

    # Initialize grid with domain wall
    simulator.grid[:, :25] = 1
    simulator.grid[:, 25:] = -1

    # Run simulation and collect snapshots
    snapshots = []
    times = [0, 100, 500, 1000]

    for step in range(max(times)):
        simulator._update_step()
        if step in times:
            snapshots.append(simulator.grid.copy())

    # Plot results
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))

    for i, (ax, grid, t) in enumerate(zip(axes, snapshots, times)):
        im = ax.imshow(grid, cmap='RdBu')
        ax.set_title(f't = {t}')
        plt.colorbar(im, ax=ax)

    plt.tight_layout()
    plt.show()

Output
------

The simulation shows:
- Domain wall formation
- Interface dynamics
- Roughening transition

.. image:: _static/domain_walls.png
   :alt: Domain walls output
   :align: center

Analysis
--------

The domain wall analysis shows:
1. Initial sharp interface
2. Interface roughening
3. Domain growth kinetics
4. Boundary effects 