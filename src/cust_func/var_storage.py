import pickle
import os

def save_kernel_state(variables, filename=None):
    if filename is None:
        # Construct path relative to this script's location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(script_dir, '..', 'storage', 'variables.pkl')
    with open(filename, 'wb') as f:
        pickle.dump(variables, f)

def load_kernel_state(filename=None):
    if filename is None:
        # Construct path relative to this script's location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(script_dir, '..', 'storage', 'variables.pkl')
    
    try:
        with open(filename, 'rb') as f:
            variables = pickle.load(f)
        return variables
    except (EOFError, pickle.UnpicklingError):
        # File is empty or corrupted, return empty dict and reinitialize
        return {}

