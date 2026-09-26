def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []

    common = set(lists[0])
    for values in lists[1:]:
        common.intersection_update(values)
        if not common:
            return []

    return sorted(common)