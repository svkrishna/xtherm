Custom Boundaries
================

This example demonstrates using different boundary conditions.

Code
----

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt
    from engine.core import ThermoSimulator
    from engine.enums import BoundaryCondition, UpdateRule

    # Create simulators with different boundaries
    boundaries = [
        BoundaryCondition.PERIODIC,
        BoundaryCondition.OPEN,
        BoundaryCondition.FIXED,
        BoundaryCondition.ANTI_PERIODIC
    ]

    simulators = [
        ThermoSimulator(
            grid_size=50,
            temperature=2.27,
            boundary=boundary,
            update_rule=UpdateRule.METROPOLIS
        )
        for boundary in boundaries
    ]

    # Run simulations
    for step in range(1000):
        for sim in simulators:
            sim._update_step()
            if step % 100 == 0:
                sim.metrics.update(sim)

    # Plot results
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    axes = axes.ravel()

    for i, (sim, boundary) in enumerate(zip(simulators, boundaries)):
        axes[i].imshow(sim.grid, cmap='RdBu')
        axes[i].set_title(f"{boundary.value} Boundary")

    plt.tight_layout()
    plt.show()

Output
------

The simulation shows:
- Different boundary effects on spin configurations
- Impact on domain formation
- Edge effects in non-periodic cases

.. image:: _static/custom_boundaries.png
   :alt: Custom boundaries output
   :align: center

Analysis
--------

The boundary conditions demonstrate:
1. Periodic: Translation invariance
2. Open: Edge effects and surface tension
3. Fixed: Boundary-induced ordering
4. Anti-periodic: Topological effects 