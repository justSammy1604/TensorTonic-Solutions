def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    n = len(values)
    result=[]

    for i in range(n - window_size + 1):
        window = values[i:i+window_size]
        avg=sum(window) / window_size
        result.append(float(avg))

    return result