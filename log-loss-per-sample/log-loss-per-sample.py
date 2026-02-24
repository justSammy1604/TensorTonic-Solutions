import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    losses=[]
    for y, p in zip(y_true, y_pred):
        p_hat = max(eps, min(1-eps, p))

        loss = -(y * math.log(p_hat) + (1 - y) * math.log(1 - p_hat))
        losses.append(loss)


    return losses