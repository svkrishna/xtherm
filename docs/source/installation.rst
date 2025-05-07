Installation
============

Requirements
-----------

xtherm requires Python 3.8 or higher and the following dependencies:

* NumPy
* SciPy
* Matplotlib
* Seaborn
* h5py
* Pandas
* Numba

Installation Methods
------------------

From PyPI
~~~~~~~~

.. code-block:: bash

   pip install xtherm

From Source
~~~~~~~~~~

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/yourusername/xtherm.git
      cd xtherm

2. Install the package:

   .. code-block:: bash

      pip install .

   Or for development:

   .. code-block:: bash

      pip install -e .

Verification
-----------

To verify the installation, run:

.. code-block:: python

   from xtherm import ThermoSimulator
   sim = ThermoSimulator(grid_size=32)
   print("Installation successful!") 