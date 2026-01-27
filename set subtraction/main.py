def find_missing_ids(first_ids, second_ids):
    first_set = set(first_ids)
    second_set = set(second_ids)

    missing_ids = set(first_set) - set(second_set)

    return missing_ids