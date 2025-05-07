Simulation Flow
==============

Overview
--------

The xtherm simulator follows a well-defined flow for running thermodynamic simulations. Here's a high-level overview of the process:

.. graphviz::

   digraph simulation_flow {
      rankdir=TB;
      node [shape=box, style=filled, fillcolor=lightblue];
      
      init [label="Initialize Simulator"];
      params [label="Set Parameters"];
      loop [label="Simulation Loop"];
      update [label="Update Grid"];
      metrics [label="Compute Metrics"];
      viz [label="Visualize/Save"];
      
      init -> params;
      params -> loop;
      loop -> update;
      update -> metrics;
      metrics -> viz;
      viz -> loop [label="continue"];
      viz -> end [label="done"];
   }

Detailed Flow
------------

1. **Initialization**
   - Create simulator instance
   - Set grid size and initial conditions
   - Configure boundary conditions
   - Choose update rule

2. **Parameter Setup**
   - Set temperature
   - Configure simulation parameters
   - Initialize metrics tracking

3. **Simulation Loop**
   - Update grid state using selected algorithm
   - Compute thermodynamic quantities
   - Track metrics and observables
   - Visualize or save state as needed

4. **State Management**
   - Save/load simulation states
   - Export results in various formats
   - Generate visualizations

Example Flow
-----------

Here's a basic example of the simulation flow:

.. code-block:: python

   from xtherm import ThermoSimulator

   # Initialize
   sim = ThermoSimulator(
       grid_size=50,
       temperature=1.0,
       boundary='periodic',
       update_rule='metropolis'
   )

   # Run simulation
   sim.run(
       steps=1000,
       plot_interval=100,
       temperature_schedule=lambda t: 2.0 * (1 - t/1000)
   )

   # Save results
   sim.save_state('results.h5') 