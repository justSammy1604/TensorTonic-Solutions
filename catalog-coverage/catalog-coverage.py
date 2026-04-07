def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    if n_items == 0:
        return 0.0

    unique_items = set()
    for rec_list in recommendations:
        unique_items.update(rec_list)

    coverage = len(unique_items) / n_items

    return float(coverage)