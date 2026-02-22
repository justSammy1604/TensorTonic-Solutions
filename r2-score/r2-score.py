import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float) 

    if y_true.shape != y_pred.shape:
        raise ValueError('Error1')
    if y_true.ndim != 1:
        raise ValueError('Error2')


    if np.all(y_true == y_true[0]):
        return 1.0 if np.allclose(y_true,y_pred) else 0.0

    sse = np.sum((y_true-y_pred) ** 2)
    sst = np.sum((y_true - np.mean(y_true)) ** 2)
    r2 = 1 - (sse / sst)

    return float(r2) 

    
