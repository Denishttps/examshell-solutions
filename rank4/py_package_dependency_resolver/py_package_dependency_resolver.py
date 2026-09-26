def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    names = set(packages)
    indegree = {name: 0 for name in names}
    dependents = {name: [] for name in names}

    for name, dependencies in packages.items():
        for dependency in set(dependencies):
            if dependency in names:
                indegree[name] += 1
                dependents[dependency].append(name)

    ready = sorted(name for name, degree in indegree.items() if degree == 0)
    order = []
    next_ready = 0

    while next_ready < len(ready):
        name = ready[next_ready]
        next_ready += 1
        order.append(name)

        for dependent in sorted(dependents[name]):
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                ready.append(dependent)

    return order if len(order) == len(names) else []