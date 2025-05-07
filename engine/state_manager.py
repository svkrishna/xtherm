"""State management for simulation persistence."""

import h5py
import pickle
import json
import numpy as np
import pandas as pd
from typing import Any, Dict
from .enums import BoundaryCondition, UpdateRule

class StateManager:
    """Manages saving and loading simulation states."""
    
    def save(self, simulator: Any, filename: str, format: str = 'h5') -> None:
        """Save simulation state to file."""
        if format == 'h5':
            self._save_h5(simulator, filename)
        elif format == 'pickle':
            self._save_pickle(simulator, filename)
        elif format == 'json':
            self._save_json(simulator, filename)
        elif format == 'npz':
            self._save_npz(simulator, filename)
        elif format == 'csv':
            self._save_csv(simulator, filename)
        else:
            raise ValueError(f"Unsupported format: {format}")
            
    def load(self, simulator: Any, filename: str, format: str = 'h5') -> None:
        """Load simulation state from file."""
        if format == 'h5':
            self._load_h5(simulator, filename)
        elif format == 'pickle':
            self._load_pickle(simulator, filename)
        elif format == 'json':
            self._load_json(simulator, filename)
        elif format == 'npz':
            self._load_npz(simulator, filename)
        elif format == 'csv':
            self._load_csv(simulator, filename)
        else:
            raise ValueError(f"Unsupported format: {format}")
            
    def _save_h5(self, simulator: Any, filename: str) -> None:
        """Save state in HDF5 format with compression."""
        with h5py.File(filename, 'w') as f:
            # Save grid with compression
            f.create_dataset('grid', data=simulator.grid, compression='gzip', compression_opts=9)
            f.create_dataset('temperature', data=simulator.temperature)
            f.create_dataset('energy', data=simulator.energy)
            f.create_dataset('magnetization', data=simulator.magnetization)
            
            # Save metrics with compression
            metrics_group = f.create_group('metrics')
            for key, value in simulator.metrics.__dict__.items():
                if isinstance(value, (list, np.ndarray)):
                    metrics_group.create_dataset(key, data=value, compression='gzip', compression_opts=9)
                else:
                    metrics_group.attrs[key] = value
                    
            # Save simulation parameters
            params_group = f.create_group('parameters')
            params_group.attrs['grid_size'] = simulator.grid_size
            params_group.attrs['boundary'] = simulator.boundary.value
            params_group.attrs['update_rule'] = simulator.update_rule.value
            
    def _save_pickle(self, simulator: Any, filename: str) -> None:
        """Save state in pickle format."""
        state = {
            'grid': simulator.grid,
            'temperature': simulator.temperature,
            'energy': simulator.energy,
            'magnetization': simulator.magnetization,
            'metrics': simulator.metrics,
            'boundary': simulator.boundary,
            'update_rule': simulator.update_rule
        }
        with open(filename, 'wb') as f:
            pickle.dump(state, f)
            
    def _save_json(self, simulator: Any, filename: str) -> None:
        """Save state in JSON format."""
        state = {
            'grid': simulator.grid.tolist(),
            'temperature': simulator.temperature,
            'energy': simulator.energy,
            'magnetization': simulator.magnetization,
            'metrics': {
                k: v if not isinstance(v, (list, np.ndarray)) else v.tolist()
                for k, v in simulator.metrics.__dict__.items()
            },
            'boundary': simulator.boundary.value,
            'update_rule': simulator.update_rule.value
        }
        with open(filename, 'w') as f:
            json.dump(state, f)
            
    def _save_npz(self, simulator: Any, filename: str) -> None:
        """Save state in compressed NumPy format."""
        np.savez_compressed(
            filename,
            grid=simulator.grid,
            temperature=simulator.temperature,
            energy=simulator.energy,
            magnetization=simulator.magnetization,
            metrics=simulator.metrics.__dict__
        )
        
    def _save_csv(self, simulator: Any, filename: str) -> None:
        """Save state in CSV format."""
        # Save grid
        np.savetxt(f"{filename}_grid.csv", simulator.grid, delimiter=',')
        
        # Save metrics
        metrics_df = pd.DataFrame(simulator.metrics.__dict__)
        metrics_df.to_csv(f"{filename}_metrics.csv", index=False)
        
        # Save parameters
        params_df = pd.DataFrame({
            'parameter': ['grid_size', 'temperature', 'boundary', 'update_rule'],
            'value': [simulator.grid_size, simulator.temperature, 
                     simulator.boundary.value, simulator.update_rule.value]
        })
        params_df.to_csv(f"{filename}_parameters.csv", index=False)
        
    def _load_h5(self, simulator: Any, filename: str) -> None:
        """Load state from HDF5 file."""
        with h5py.File(filename, 'r') as f:
            simulator.grid = f['grid'][:]
            simulator.temperature = f['temperature'][()]
            simulator.energy = f['energy'][()]
            simulator.magnetization = f['magnetization'][()]
            
            # Load metrics
            metrics_group = f['metrics']
            for key in metrics_group.keys():
                if isinstance(metrics_group[key], h5py.Dataset):
                    setattr(simulator.metrics, key, metrics_group[key][:])
                else:
                    setattr(simulator.metrics, key, metrics_group[key].attrs[key])
                    
            # Load parameters
            params_group = f['parameters']
            simulator.grid_size = params_group.attrs['grid_size']
            simulator.boundary = BoundaryCondition(params_group.attrs['boundary'])
            simulator.update_rule = UpdateRule(params_group.attrs['update_rule'])
            
    def _load_pickle(self, simulator: Any, filename: str) -> None:
        """Load state from pickle file."""
        with open(filename, 'rb') as f:
            state = pickle.load(f)
            
        simulator.grid = state['grid']
        simulator.temperature = state['temperature']
        simulator.energy = state['energy']
        simulator.magnetization = state['magnetization']
        simulator.metrics = state['metrics']
        simulator.boundary = state['boundary']
        simulator.update_rule = state['update_rule']
        
    def _load_json(self, simulator: Any, filename: str) -> None:
        """Load state from JSON file."""
        with open(filename, 'r') as f:
            state = json.load(f)
            
        simulator.grid = np.array(state['grid'])
        simulator.temperature = state['temperature']
        simulator.energy = state['energy']
        simulator.magnetization = state['magnetization']
        
        # Load metrics
        for key, value in state['metrics'].items():
            if isinstance(value, list):
                setattr(simulator.metrics, key, np.array(value))
            else:
                setattr(simulator.metrics, key, value)
                
        simulator.boundary = BoundaryCondition(state['boundary'])
        simulator.update_rule = UpdateRule(state['update_rule'])
        
    def _load_npz(self, simulator: Any, filename: str) -> None:
        """Load state from compressed NumPy file."""
        data = np.load(filename)
        simulator.grid = data['grid']
        simulator.temperature = data['temperature']
        simulator.energy = data['energy']
        simulator.magnetization = data['magnetization']
        
        # Load metrics
        for key, value in data['metrics'].item().items():
            setattr(simulator.metrics, key, value)
            
    def _load_csv(self, simulator: Any, filename: str) -> None:
        """Load state from CSV files."""
        # Load grid
        simulator.grid = np.loadtxt(f"{filename}_grid.csv", delimiter=',')
        
        # Load metrics
        metrics_df = pd.read_csv(f"{filename}_metrics.csv")
        for column in metrics_df.columns:
            setattr(simulator.metrics, column, metrics_df[column].values)
            
        # Load parameters
        params_df = pd.read_csv(f"{filename}_parameters.csv")
        simulator.grid_size = int(params_df[params_df['parameter'] == 'grid_size']['value'].iloc[0])
        simulator.temperature = float(params_df[params_df['parameter'] == 'temperature']['value'].iloc[0])
        simulator.boundary = BoundaryCondition(params_df[params_df['parameter'] == 'boundary']['value'].iloc[0])
        simulator.update_rule = UpdateRule(params_df[params_df['parameter'] == 'update_rule']['value'].iloc[0]) 