# XTherm - Thermodynamic Computing Simulator

XTherm is a powerful and flexible Python package for simulating thermodynamic systems, with a particular focus on the Ising model and related statistical physics models. It provides a comprehensive suite of tools for studying phase transitions, critical phenomena, and complex thermodynamic behaviors.

## Features

- **Multiple Update Algorithms**
  - Metropolis-Hastings
  - Glauber dynamics
  - Heat bath
  - Wolff cluster algorithm
  - Swendsen-Wang
  - Kawasaki dynamics
  - And more...

- **Advanced Simulation Capabilities**
  - Parallel tempering
  - Multi-canonical sampling
  - Wang-Landau algorithm
  - Custom boundary conditions
  - Mixed boundary configurations

- **Comprehensive Metrics**
  - Energy and magnetization tracking
  - Specific heat and susceptibility
  - Binder cumulant
  - Correlation length
  - Entropy and free energy
  - Critical exponents
  - Fisher and Lee-Yang zeros

- **Performance Optimizations**
  - Numba-accelerated computations
  - Parallel processing support
  - Efficient state management
  - Optimized data structures

- **Visualization Tools**
  - Real-time simulation visualization
  - Phase transition plots
  - Critical phenomena analysis
  - Domain wall dynamics
  - Custom plotting capabilities

- **State Management**
  - Multiple file format support (HDF5, NPZ, CSV)
  - Simulation state persistence
  - Efficient data compression
  - Easy state restoration

## Installation

```bash
pip install xtherm
```

## Quick Start

```python
from xtherm import ThermoSimulator
from xtherm.engine.enums import BoundaryCondition, UpdateRule

# Initialize simulator
simulator = ThermoSimulator(
    grid_size=50,
    temperature=2.27,  # Critical temperature for 2D Ising model
    boundary=BoundaryCondition.PERIODIC,
    update_rule=UpdateRule.METROPOLIS
)

# Run simulation
simulator.run(steps=1000, plot_interval=100)
```

## Documentation

Full documentation is available at [ReadTheDocs](https://xtherm.readthedocs.io/).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use XTherm in your research, please cite:

```bibtex
@software{xtherm2024,
  author = {Your Name},
  title = {XTherm: Thermodynamic Computing Simulator},
  year = {2024},
  url = {https://github.com/yourusername/xtherm}
}
``` 