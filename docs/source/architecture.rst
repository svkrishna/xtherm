Architecture
============

Component Diagram
----------------

.. mermaid::

    graph TB
        subgraph Core Engine
            CE[Core Engine]
            TM[Thermodynamics Module]
            EN[Enums]
            CE --> TM
            CE --> EN
        end

        subgraph State Management
            SM[State Manager]
            SM --> |HDF5| CE
            SM --> |NPZ| CE
            SM --> |CSV| CE
        end

        subgraph Visualization
            PL[Plotter]
            PL --> |Real-time| CE
            PL --> |Analysis| TM
        end

        subgraph Scheduling
            SC[Scheduler]
            SC --> |Temperature| CE
            SC --> |Parallel| CE
        end

        subgraph CLI
            CLI[Command Line Interface]
            CLI --> CE
            CLI --> SM
            CLI --> PL
            CLI --> SC
        end

        subgraph Performance
            NB[Numba Acceleration]
            PR[Parallel Processing]
            NB --> |JIT| CE
            NB --> |JIT| TM
            PR --> |Multi-core| CE
            PR --> |MPI| SC
        end

        classDef core fill:#f9f,stroke:#333,stroke-width:2px
        classDef state fill:#bbf,stroke:#333,stroke-width:2px
        classDef viz fill:#bfb,stroke:#333,stroke-width:2px
        classDef sched fill:#fbb,stroke:#333,stroke-width:2px
        classDef cli fill:#fbf,stroke:#333,stroke-width:2px
        classDef perf fill:#ff9,stroke:#333,stroke-width:2px

        class CE,TM,EN core
        class SM state
        class PL viz
        class SC sched
        class CLI cli
        class NB,PR perf

Component Descriptions
---------------------

Core Engine
~~~~~~~~~~

The core engine is the heart of XTherm, responsible for:

- Grid initialization and management
- Spin update algorithms
- Energy and magnetization calculations
- Boundary condition handling
- Numba-accelerated computations

State Management
~~~~~~~~~~~~~~

Handles persistence and data management:

- Multiple file format support (HDF5, NPZ, CSV)
- Efficient data compression
- State serialization/deserialization
- Checkpoint management

Visualization
~~~~~~~~~~~

Provides real-time and analysis visualization:

- Grid state visualization
- Energy and magnetization plots
- Phase transition analysis
- Custom plotting capabilities
- Real-time updates

Scheduling
~~~~~~~~~

Manages simulation scheduling and optimization:

- Temperature scheduling
- Parallel tempering
- Multi-canonical sampling
- MPI-based parallelization
- Adaptive scheduling

CLI
~~~

Command-line interface for:

- Simulation configuration
- Parameter management
- Batch processing
- Result analysis
- State management

Performance Optimizations
~~~~~~~~~~~~~~~~~~~~~~

Key performance features:

- Numba JIT compilation for core algorithms
- Multi-core parallel processing
- MPI support for distributed computing
- Optimized data structures
- Efficient memory management

Data Flow
--------

1. **Initialization Flow**:
   - CLI/User configures simulation
   - Core Engine initializes grid
   - State Manager loads/saves configuration

2. **Simulation Flow**:
   - Scheduler manages temperature/parameters
   - Core Engine performs updates
   - Thermodynamics Module computes metrics
   - Plotter visualizes results
   - State Manager saves checkpoints

3. **Analysis Flow**:
   - State Manager loads results
   - Plotter generates analysis plots
   - CLI provides analysis tools

Performance Considerations
------------------------

- Numba acceleration is applied to:
  - Grid update algorithms
  - Energy calculations
  - Thermodynamic quantity computations
  - Correlation functions

- Parallel processing is used for:
  - Multi-replica simulations
  - Large grid updates
  - Batch processing
  - Distributed computing 