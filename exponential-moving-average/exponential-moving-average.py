def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    ema = [float(values[0])]

    for i in range(1, len(values)):
        current_ema = alpha * values[i] + (1 - alpha) * ema[-1]
        ema.append(float(current_ema))

    return ema