def activity_selection(activities):
    activities.sort(key=lambda x: x[1])  # Sort by finish time
    selected = []
    last_end = 0

    for start, end in activities:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected


