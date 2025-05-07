Algorithms
=========

Update Rules
-----------

xtherm implements various update rules for simulating thermodynamic systems:

Metropolis
~~~~~~~~~

The classic Metropolis algorithm for single-spin updates:

.. math::

   P(accept) = \min(1, e^{-\Delta E/T})

where :math:`\Delta E` is the energy change and :math:`T` is the temperature.

Glauber
~~~~~~~

The Glauber dynamics update rule:

.. math::

   P(accept) = \frac{1}{1 + e^{\Delta E/T}}

Heat Bath
~~~~~~~~

The heat bath algorithm for thermal equilibrium:

.. math::

   P(up) = \frac{1}{1 + e^{-2\beta h}}

where :math:`\beta = 1/T` and :math:`h` is the local field.

Wolff
~~~~~

Cluster update algorithm that grows clusters of aligned spins:

1. Pick a random seed spin
2. Add neighboring spins to cluster with probability :math:`P = 1 - e^{-2\beta J}`
3. Flip the entire cluster

Swendsen-Wang
~~~~~~~~~~~~

Another cluster algorithm that:

1. Identify bonds between aligned spins
2. Form clusters based on bond probabilities
3. Flip entire clusters independently

Kawasaki
~~~~~~~~

Conserves magnetization by swapping pairs of spins:

1. Select two spins
2. Calculate energy change
3. Accept/reject based on Metropolis criterion

Boundary Conditions
-----------------

The simulator supports various boundary conditions:

Periodic
~~~~~~~~

Spins at opposite edges are connected, creating a toroidal topology.

Open
~~~~

No connections at boundaries, effectively creating edges.

Fixed
~~~~~

Boundary spins are fixed to a specific value (usually +1 or -1).

Anti-periodic
~~~~~~~~~~~~

Opposite edges are connected with a sign flip.

Mixed
~~~~~

Different boundary conditions on different edges.

Implementation Details
--------------------

Each algorithm is implemented with Numba acceleration for optimal performance:

.. code-block:: python

   @jit(nopython=True)
   def _update_metropolis(grid, temperature):
       # Implementation details
       pass

Performance Considerations
------------------------

* Single-spin updates (Metropolis, Glauber) are efficient for high temperatures
* Cluster updates (Wolff, Swendsen-Wang) are better near critical points
* Kawasaki dynamics is useful for conserved order parameters
* Boundary conditions can significantly affect phase transitions 