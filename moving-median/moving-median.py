def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    n=len(values)
    result=[]

    for i in range(n-window_size + 1):
        window = values[i:i+window_size]
        sorted_window = sorted(window)

        if window_size % 2 == 1:
            median = float(sorted_window[window_size // 2])
        else:
            mid1 = sorted_window[window_size // 2 - 1]
            mid2 = sorted_window[window_size // 2]
            median = (mid1 + mid2) / 2.0

        result.append(median)

    return result