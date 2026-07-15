import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    up = np.dot(a,b)
    down = np.linalg.norm(a) * np.linalg.norm(b)

    if down == 0:
        return 0
    else:
        res = up / down
        return res
    pass