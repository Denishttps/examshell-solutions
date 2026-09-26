import heapq


def py_room_scheduler(meetings: list[list[int]]) -> dict[str, object]:
    if not meetings:
        return {"total_rooms": 0, "schedule": []}

    occupied = []
    available = []
    schedule = []

    for start, end in sorted(meetings, key=lambda interval: interval[0]):
        while occupied and occupied[0][0] <= start:
            _, room_index = heapq.heappop(occupied)
            heapq.heappush(available, room_index)

        if available:
            room_index = heapq.heappop(available)
        else:
            room_index = len(schedule)
            schedule.append([])

        schedule[room_index].append([start, end])
        heapq.heappush(occupied, (end, room_index))

    return {"total_rooms": len(schedule), "schedule": schedule}