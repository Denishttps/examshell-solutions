import heapq


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    heap = []
    for list_index, values in enumerate(lists):
        if values:
            heapq.heappush(heap, (values[0], list_index, 0))

    result = []
    while heap:
        value, list_index, element_index = heapq.heappop(heap)
        result.append(value)
        next_index = element_index + 1
        if next_index < len(lists[list_index]):
            heapq.heappush(
                heap,
                (lists[list_index][next_index], list_index, next_index),
            )

    return result