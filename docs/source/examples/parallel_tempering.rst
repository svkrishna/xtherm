Parallel Tempering
=================

This example demonstrates parallel tempering simulation.

Code
----

.. code-block:: python

    import numpy as np
    from engine.core import ThermoSimulator
    from engine.enums import BoundaryCondition, UpdateRule
    from parallel.tempering import ParallelTempering

    # Initialize parallel tempering
    temperatures = np.linspace(1.0, 4.0, 8)
    simulators = [
        ThermoSimulator(
            grid_size=50,
            temperature=T,
            boundary=BoundaryCondition.PERIODIC,
            update_rule=UpdateRule.METROPOLIS
        )
        for T in temperatures
    ]

    # Create parallel tempering instance
    pt = ParallelTempering(simulators)

    # Run simulation
    for step in range(1000):
        # Update all replicas
        for sim in simulators:
            sim._update_step()

        # Attempt replica exchange
        if step % 10 == 0:
            pt.attempt_exchange()

        # Update metrics
        if step % 100 == 0:
            for sim in simulators:
                sim.metrics.update(sim)

Output
------

The simulation produces:
- Multiple replicas at different temperatures
- Replica exchange statistics
- Energy and magnetization distributions

.. image:: _static/parallel_tempering.png
   :alt: Parallel tempering output
   :align: center

Analysis
--------

The parallel tempering simulation shows:
1. Enhanced sampling across temperature range
2. Improved convergence through replica exchange
3. Temperature-dependent phase behavior 