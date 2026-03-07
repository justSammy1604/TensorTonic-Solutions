def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    A = set(set_a)
    B = set(set_b)

    union = A | B

    if len(union) == 0:
        return 0.0

    intersection = A & B

    jac = len(intersection) / len(union)

    return float(jac)
    