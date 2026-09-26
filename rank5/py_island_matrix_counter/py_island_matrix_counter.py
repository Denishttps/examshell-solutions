def island_matrix_counter(matrix: list[list[str]]) -> int:
    if not matrix:
        return 0

    visited = set()
    island_count = 0
    for row_index, row in enumerate(matrix):
        for col_index, cell in enumerate(row):
            if cell != "1" or (row_index, col_index) in visited:
                continue

            island_count += 1
            stack = [(row_index, col_index)]
            visited.add((row_index, col_index))
            while stack:
                row, col = stack.pop()
                for next_row, next_col in (
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ):
                    if (
                        0 <= next_row < len(matrix)
                        and 0 <= next_col < len(matrix[next_row])
                        and matrix[next_row][next_col] == "1"
                        and (next_row, next_col) not in visited
                    ):
                        visited.add((next_row, next_col))
                        stack.append((next_row, next_col))

    return island_count