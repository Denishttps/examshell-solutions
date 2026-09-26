def prism_detector(grid: list[str], pattern: str) -> list[tuple[int, int, str]]:
    if not grid or not pattern:
        return []

    directions = (
        (1, 0, "H"),
        (-1, 0, "H-"),
        (0, 1, "V"),
        (0, -1, "V-"),
        (1, 1, "D1"),
        (-1, -1, "D1-"),
        (-1, 1, "D2"),
        (1, -1, "D2-"),
    )
    matches = []

    for row, line in enumerate(grid):
        for col in range(len(line)):
            for delta_col, delta_row, code in directions:
                for offset, char in enumerate(pattern):
                    target_row = row + delta_row * offset
                    target_col = col + delta_col * offset
                    if (
                        target_row < 0
                        or target_row >= len(grid)
                        or target_col < 0
                        or target_col >= len(grid[target_row])
                        or grid[target_row][target_col] != char
                    ):
                        break
                else:
                    matches.append((col, row, code))

    return matches