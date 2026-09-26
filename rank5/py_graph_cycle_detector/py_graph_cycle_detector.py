def py_graph_cycle_detector(graph: dict[int, list[int]]) -> bool:
    state = {}

    def has_cycle(node: int) -> bool:
        current_state = state.get(node, 0)
        if current_state == 1:
            return True
        if current_state == 2:
            return False

        state[node] = 1
        for neighbor in graph.get(node, []):
            if has_cycle(neighbor):
                return True
        state[node] = 2
        return False

    nodes = set(graph)
    for neighbors in graph.values():
        nodes.update(neighbors)

    return any(has_cycle(node) for node in nodes if state.get(node, 0) == 0)