from collections import defaultdict, deque


def word_ladder(start: str, end: str, sentence: list[str]) -> int:
    if start == end:
        return 1

    words = {word for word in sentence if len(word) == len(start)}
    if end not in words:
        return 0

    patterns = defaultdict(list)
    for word in words:
        for index in range(len(word)):
            patterns[(index, word[:index], word[index + 1:])].append(word)

    queue = deque([(start, 1)])
    visited = {start}
    while queue:
        word, distance = queue.popleft()
        for index in range(len(word)):
            pattern = (index, word[:index], word[index + 1:])
            for neighbor in patterns[pattern]:
                if neighbor == end:
                    return distance + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
            patterns[pattern].clear()

    return 0