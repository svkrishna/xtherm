Critical Phenomena
=================

This example demonstrates critical phenomena in the Ising model.

Code
----

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt
    from engine.core import ThermoSimulator
    from engine.enums import BoundaryCondition, UpdateRule

    # Parameters
    grid_sizes = [16, 32, 64, 128]
    T_c = 2.27  # Critical temperature
    delta_T = 0.1
    temperatures = np.linspace(T_c - delta_T, T_c + delta_T, 20)
    steps = 1000
    equilibration = 500

    # Arrays for finite-size scaling
    binder_cumulants = {L: [] for L in grid_sizes}
    magnetizations = {L: [] for L in grid_sizes}
    susceptibilities = {L: [] for L in grid_sizes}

    for L in grid_sizes:
        print(f"Processing grid size {L}")
        for T in temperatures:
            # Initialize simulator
            sim = ThermoSimulator(
                grid_size=L,
                temperature=T,
                boundary=BoundaryCondition.PERIODIC,
                update_rule=UpdateRule.METROPOLIS
            )

            # Equilibration
            for _ in range(equilibration):
                sim._update_step()

            # Measurement
            M_samples = []
            for _ in range(steps):
                sim._update_step()
                M_samples.append(sim.magnetization)

            # Compute observables
            M = np.mean(np.abs(M_samples))
            M2 = np.mean(np.array(M_samples) ** 2)
            M4 = np.mean(np.array(M_samples) ** 4)
            chi = (M2 - M * M) * L * L / T
            U = 1 - M4 / (3 * M2 * M2)

            magnetizations[L].append(M)
            susceptibilities[L].append(chi)
            binder_cumulants[L].append(U)

    # Plot results
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

    for L in grid_sizes:
        ax1.plot(temperatures, magnetizations[L], 
                label=f'L={L}')
        ax2.plot(temperatures, susceptibilities[L], 
                label=f'L={L}')
        ax3.plot(temperatures, binder_cumulants[L], 
                label=f'L={L}')

    ax1.set_xlabel('Temperature')
    ax1.set_ylabel('Magnetization')
    ax1.legend()

    ax2.set_xlabel('Temperature')
    ax2.set_ylabel('Susceptibility')
    ax2.legend()

    ax3.set_xlabel('Temperature')
    ax3.set_ylabel('Binder Cumulant')
    ax3.legend()

    plt.tight_layout()
    plt.show()

Output
------

The simulation produces:
- Finite-size scaling plots
- Critical exponents
- Universal quantities

.. image:: _static/critical_phenomena.png
   :alt: Critical phenomena output
   :align: center

Analysis
--------

The critical phenomena analysis shows:
1. Universal scaling functions
2. Critical exponents (β, γ, ν)
3. Finite-size effects
4. Binder cumulant crossing 