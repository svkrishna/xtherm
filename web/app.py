"""Streamlit web interface for XTherm."""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from xtherm import ThermoSimulator
from xtherm.engine.enums import BoundaryCondition, UpdateRule

st.set_page_config(
    page_title="XTherm Simulator",
    page_icon="🌡️",
    layout="wide"
)

def main():
    st.title("XTherm - Thermodynamic Computing Simulator")
    
    # Sidebar controls
    st.sidebar.header("Simulation Parameters")
    
    # Grid size
    grid_size = st.sidebar.slider(
        "Grid Size",
        min_value=20,
        max_value=200,
        value=50,
        step=10
    )
    
    # Temperature
    temperature = st.sidebar.slider(
        "Temperature",
        min_value=0.1,
        max_value=5.0,
        value=2.27,
        step=0.01
    )
    
    # Boundary condition
    boundary = st.sidebar.selectbox(
        "Boundary Condition",
        options=list(BoundaryCondition),
        format_func=lambda x: x.value
    )
    
    # Update rule
    update_rule = st.sidebar.selectbox(
        "Update Rule",
        options=list(UpdateRule),
        format_func=lambda x: x.value
    )
    
    # Simulation steps
    steps = st.sidebar.slider(
        "Simulation Steps",
        min_value=100,
        max_value=10000,
        value=1000,
        step=100
    )
    
    # Plot interval
    plot_interval = st.sidebar.slider(
        "Plot Interval",
        min_value=1,
        max_value=100,
        value=10,
        step=1
    )
    
    # Initialize simulator
    if 'simulator' not in st.session_state:
        st.session_state.simulator = ThermoSimulator(
            grid_size=grid_size,
            temperature=temperature,
            boundary=boundary,
            update_rule=update_rule
        )
    
    # Run simulation
    if st.sidebar.button("Run Simulation"):
        with st.spinner("Running simulation..."):
            st.session_state.simulator.run(
                steps=steps,
                plot_interval=plot_interval
            )
    
    # Display results
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Spin Configuration")
        fig, ax = plt.subplots(figsize=(6, 6))
        im = ax.imshow(
            st.session_state.simulator.grid,
            cmap='RdBu',
            vmin=-1,
            vmax=1
        )
        plt.colorbar(im, ax=ax)
        st.pyplot(fig)
        plt.close()
    
    with col2:
        st.subheader("Thermodynamic Quantities")
        
        # Energy plot
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.plot(st.session_state.simulator.metrics.energy_history)
        ax.set_xlabel("Step")
        ax.set_ylabel("Energy")
        st.pyplot(fig)
        plt.close()
        
        # Magnetization plot
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.plot(st.session_state.simulator.metrics.magnetization_history)
        ax.set_xlabel("Step")
        ax.set_ylabel("Magnetization")
        st.pyplot(fig)
        plt.close()
    
    # Metrics
    st.subheader("Simulation Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Energy",
            f"{st.session_state.simulator.energy:.2f}"
        )
    
    with col2:
        st.metric(
            "Magnetization",
            f"{st.session_state.simulator.magnetization:.2f}"
        )
    
    with col3:
        st.metric(
            "Acceptance Rate",
            f"{st.session_state.simulator.metrics.acceptance_rate:.2%}"
        )
    
    with col4:
        st.metric(
            "Temperature",
            f"{temperature:.2f}"
        )
    
    # Save state
    if st.sidebar.button("Save State"):
        st.session_state.simulator.save_state("simulation_state.h5")
        st.sidebar.success("State saved successfully!")

if __name__ == "__main__":
    main() 