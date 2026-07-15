import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    x_arr = np.array(x)
    res = np.maximum(0, x_arr)
    return res
    pass