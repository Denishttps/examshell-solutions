from collections import deque


def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if k <= 0 or k > len(nums):
        return []

    candidates = deque()
    result = []
    for index, value in enumerate(nums):
        while candidates and candidates[0] <= index - k:
            candidates.popleft()
        while candidates and nums[candidates[-1]] <= value:
            candidates.pop()
        candidates.append(index)

        if index >= k - 1:
            result.append(nums[candidates[0]])

    return result