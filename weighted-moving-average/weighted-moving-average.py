def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here
    k = len(weights)
    w_sum = sum(weights)
    result = []

    for i in range(len(values) - k + 1):
        wght_sum = sum(weights[j] * values[i+j] for j in range(k))
        result.append(wght_sum / w_sum)

    return result