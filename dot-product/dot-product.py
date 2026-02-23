import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    if len(x) != len(y):
        raise ValueError
    
    x = np.array(x)
    y = np.array(y)

    
    
    odd_index_x = x[1::2]
    even_index_x = x[0::2]

    odd_index_y = y[1::2]
    even_index_y = y[0::2]
    
    # Write code here
    res = sum(odd_index_x*odd_index_y) + sum(even_index_x*even_index_y)
    return float(res)
    pass
