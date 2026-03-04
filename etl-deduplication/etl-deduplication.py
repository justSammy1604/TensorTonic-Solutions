def deduplicate(records, key_columns, strategy):
    """
    Deduplicate records by key columns using the given strategy.
    """
    # Write code here
    if strategy not in {"first", "last", "most_complete"}:
        raise ValueError("Invalid strategy")

    # Dictionary to store:
    # key -> (selected_record, index_of_first_occurrence)
    selected = {}
    first_index = {}

    for idx, record in enumerate(records):
        # Build composite key (tuple works for single or multiple keys)
        key = tuple(record.get(col) for col in key_columns)

        if key not in selected:
            selected[key] = record
            first_index[key] = idx
        else:
            if strategy == "first":
                continue

            elif strategy == "last":
                selected[key] = record

            elif strategy == "most_complete":
                current_best = selected[key]

                # Count None values across ALL fields
                current_none_count = sum(v is None for v in current_best.values())
                new_none_count = sum(v is None for v in record.values())

                # Fewer None values wins
                if new_none_count < current_none_count:
                    selected[key] = record
                # Tie → keep first (do nothing)

    # Sort keys by first appearance index
    ordered_keys = sorted(first_index.keys(), key=lambda k: first_index[k])

    # Return selected records in correct order
    return [selected[key] for key in ordered_keys]
    