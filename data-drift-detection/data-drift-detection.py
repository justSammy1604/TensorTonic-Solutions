def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here
    ref_total = sum(reference_counts)
    prod_total = sum(production_counts)

    ref_probs = [c / ref_total for c in reference_counts]
    prod_probs = [c / prod_total for c in production_counts]

    tvd = 0.5 * sum(abs(p - q) for p,q in zip(ref_probs, prod_probs))

    drift_detect = tvd > threshold 

    return {
        'score':tvd,
        "drift_detected":drift_detect
    }
