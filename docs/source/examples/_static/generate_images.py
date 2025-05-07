"""Generate example images for documentation."""

import numpy as np
import matplotlib.pyplot as plt
from engine.core import ThermoSimulator
from engine.enums import BoundaryCondition, UpdateRule
from viz.plotter import Plotter

def generate_basic_simulation():
    """Generate basic simulation image."""
    simulator = ThermoSimulator(
        grid_size=50,
        temperature=1.0,
        boundary=BoundaryCondition.PERIODIC,
        update_rule=UpdateRule.METROPOLIS
    )

    # Run simulation
    simulator.run(steps=1000, plot_interval=100)
    plt.savefig('basic_simulation.png', dpi=300, bbox_inches='tight')
    plt.close()

def generate_visualization():
    """Generate visualization image."""
    simulator = ThermoSimulator(
        grid_size=50,
        temperature=2.27,
        boundary=BoundaryCondition.PERIODIC,
        update_rule=UpdateRule.METROPOLIS
    )

    # Create custom plotter
    plotter = Plotter(simulator)

    # Run simulation
    for step in range(1000):
        simulator._update_step()
        if step % 10 == 0:
            simulator.metrics.update(simulator)
            plotter.update()

    plt.savefig('visualization.png', dpi=300, bbox_inches='tight')
    plt.close()

def generate_parallel_tempering():
    """Generate parallel tempering image."""
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

    # Run simulation
    for step in range(1000):
        for sim in simulators:
            sim._update_step()
            if step % 100 == 0:
                sim.metrics.update(sim)

    # Plot results
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    axes = axes.ravel()

    for i, (sim, T) in enumerate(zip(simulators, temperatures)):
        axes[i].imshow(sim.grid, cmap='RdBu')
        axes[i].set_title(f'T = {T:.2f}')

    plt.tight_layout()
    plt.savefig('parallel_tempering.png', dpi=300, bbox_inches='tight')
    plt.close()

def generate_custom_boundaries():
    """Generate custom boundaries image."""
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
    plt.savefig('custom_boundaries.png', dpi=300, bbox_inches='tight')
    plt.close()

def generate_phase_transitions():
    """Generate phase transitions image."""
    temperatures = np.linspace(1.0, 4.0, 20)
    grid_size = 50
    steps = 1000
    equilibration = 500

    energies = []
    magnetizations = []
    specific_heats = []
    susceptibilities = []

    for T in temperatures:
        sim = ThermoSimulator(
            grid_size=grid_size,
            temperature=T,
            boundary=BoundaryCondition.PERIODIC,
            update_rule=UpdateRule.METROPOLIS
        )

        # Equilibration
        for _ in range(equilibration):
            sim._update_step()

        # Measurement
        E_samples = []
        M_samples = []
        for _ in range(steps):
            sim._update_step()
            E_samples.append(sim.energy)
            M_samples.append(abs(sim.magnetization))

        # Compute observables
        E_mean = np.mean(E_samples)
        M_mean = np.mean(M_samples)
        C = np.var(E_samples) / (T * T)
        chi = np.var(M_samples) / T

        energies.append(E_mean)
        magnetizations.append(M_mean)
        specific_heats.append(C)
        susceptibilities.append(chi)

    # Plot results
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 12))

    ax1.plot(temperatures, energies)
    ax1.set_xlabel('Temperature')
    ax1.set_ylabel('Energy')

    ax2.plot(temperatures, magnetizations)
    ax2.set_xlabel('Temperature')
    ax2.set_ylabel('|Magnetization|')

    ax3.plot(temperatures, specific_heats)
    ax3.set_xlabel('Temperature')
    ax3.set_ylabel('Specific Heat')

    ax4.plot(temperatures, susceptibilities)
    ax4.set_xlabel('Temperature')
    ax4.set_ylabel('Susceptibility')

    plt.tight_layout()
    plt.savefig('phase_transitions.png', dpi=300, bbox_inches='tight')
    plt.close()

def generate_critical_phenomena():
    """Generate critical phenomena image."""
    grid_sizes = [16, 32, 64, 128]
    T_c = 2.27
    delta_T = 0.1
    temperatures = np.linspace(T_c - delta_T, T_c + delta_T, 20)
    steps = 1000
    equilibration = 500

    binder_cumulants = {L: [] for L in grid_sizes}
    magnetizations = {L: [] for L in grid_sizes}
    susceptibilities = {L: [] for L in grid_sizes}

    for L in grid_sizes:
        print(f"Processing grid size {L}")
        for T in temperatures:
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
        ax1.plot(temperatures, magnetizations[L], label=f'L={L}')
        ax2.plot(temperatures, susceptibilities[L], label=f'L={L}')
        ax3.plot(temperatures, binder_cumulants[L], label=f'L={L}')

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
    plt.savefig('critical_phenomena.png', dpi=300, bbox_inches='tight')
    plt.close()

def generate_domain_walls():
    """Generate domain walls image."""
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
    plt.savefig('domain_walls.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    print("Generating example images...")
    generate_basic_simulation()
    generate_visualization()
    generate_parallel_tempering()
    generate_custom_boundaries()
    generate_phase_transitions()
    generate_critical_phenomena()
    generate_domain_walls()
    print("Done!") 