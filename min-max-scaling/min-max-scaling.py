def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    rows=len(data)
    cols = len(data[0])

    res = [[0.0 for _ in range(cols)] for _ in range(rows)]

    for j in range(cols):
        column = [data[i][j] for i in range(rows)]
        min_val = min(column)
        max_val = max(column)
        range_val = max_val - min_val

        if range_val == 0:
            continue
        else:
            for i in range(rows):
                res[i][j] = (data[i][j] - min_val) / range_val

    return res