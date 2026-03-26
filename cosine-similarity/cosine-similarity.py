import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)
    
    tu_so = a@b
    mau_so = np.linalg.norm(a) * np.linalg.norm(b)
    res = tu_so / mau_so
    if mau_so == 0:
        return 0
    else:
        return res
    pass