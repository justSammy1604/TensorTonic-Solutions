import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)

    if y_true.shape != y_score.shape:
        raise ValueError('Error')

    if not np.all(np.isin(y_true, [-1, 1])):
        raise ValueError('Error')

    loss = np.maximum(0, margin-y_true*y_score)

    if reduction == 'mean':
        return float(loss.mean())
    elif reduction == 'sum':
        return float(loss.sum())
    else:
        raise ValueError('Error')