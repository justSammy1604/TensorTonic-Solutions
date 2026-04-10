import numpy as np
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    result = []

    for v in values:
        result.append(np.log(1 + v))


    return result