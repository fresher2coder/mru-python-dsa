def activity_selection(activities):
    # [(3, 5), (1, 2), (6, 8), (4, 7)]
    #[(1, 2), (3, 5), (4, 7), (6, 8)]
    activities.sort(key=lambda x:x[1])
    selected = []
    last_end = 0

    for start, end in activities:

        if start>=last_end:
            selected.append((start, end))
            last_end = end
    return selected



