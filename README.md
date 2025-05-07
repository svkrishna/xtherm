# XTherm - Thermodynamic Computing Simulator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/xtherm.svg)](https://badge.fury.io/py/xtherm)
[![Build Status](https://github.com/yourusername/xtherm/actions/workflows/main.yml/badge.svg)](https://github.com/yourusername/xtherm/actions/workflows/main.yml)
[![Documentation Status](https://readthedocs.org/projects/xtherm/badge/?version=latest)](https://xtherm.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/yourusername/xtherm/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/xtherm)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

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

## Python Support

XTherm requires Python 3.8 or higher. This requirement is due to:

- Type hinting features introduced in Python 3.8
- Numba compatibility requirements
- Modern Python features used in the codebase
- Performance optimizations that leverage Python 3.8+ capabilities

### Key Dependencies

- NumPy ≥ 1.20.0
- SciPy ≥ 1.7.0
- Numba ≥ 0.54.0
- Matplotlib ≥ 3.4.0
- h5py ≥ 3.3.0

## Examples and Tutorials

Check out our Jupyter notebooks for interactive examples:

- [Basic Ising Model](examples/ising_basics.ipynb): Introduction to XTherm with a simple Ising model simulation
- [Phase Transition Analysis](examples/phase_transition_map.ipynb): Study phase transitions and critical phenomena

To run the notebooks:

```bash
# Install Jupyter
pip install jupyter

# Clone the repository
git clone https://github.com/yourusername/xtherm.git
cd xtherm

# Start Jupyter
jupyter notebook
```

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