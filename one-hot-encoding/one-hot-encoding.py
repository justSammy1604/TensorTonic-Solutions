import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here
    y = np.asarray(y)

    if num_classes is None:
        num_classes = np.max(y) + 1

    if np.any(y < 0) or np.any(y >= num_classes):
        raise ValueError('Error1')

    N = y.shape[0]
    Y = np.zeros((N, num_classes), dtype=float)

    Y[np.arange(N), y] = 1.0

    return Y
