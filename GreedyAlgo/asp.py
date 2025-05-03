def activitySelection(start, finish):
    selected_activities = []
    arr = sorted([(finish[i], start[i]) for i in range(len(start))])
    finishtime = -1
    for f, s in arr:
        if s >= finishtime:
            finishtime = f
            selected_activities.append((s, f))
    return selected_activities


def displayActivitiesTable(start, finish):
    header = [""] + [str(i + 1) for i in range(len(start))]
    starts = ["Start"] + [str(s) for s in start]
    finishes = ["Finish"] + [str(f) for f in finish]

    print("\t".join(header))
    print("\t".join(starts))
    print("\t".join(finishes))
    print()


def displayActivitiesTableFromPairs(pairs):
    header = [""] + [str(i + 1) for i in range(len(pairs))]
    starts = ["Start"] + [str(s) for s, f in pairs]
    finishes = ["Finish"] + [str(f) for s, f in pairs]

    print("\t".join(header))
    print("\t".join(starts))
    print("\t".join(finishes))
    print()


def displaySortedActivitiesTable(start, finish):
    arr = sorted([(finish[i], start[i]) for i in range(len(start))])
    pairs = [(s, f) for f, s in arr]
    displayActivitiesTableFromPairs(pairs)


if __name__ == "__main__":
    start = [0, 3, 1, 5, 5, 8]
    finish = [6, 4, 2, 9, 7, 9]

    print("All Activities:")
    displayActivitiesTable(start, finish)

    print("Sorted Activities by Finish Time:")
    displaySortedActivitiesTable(start, finish)

    selected = activitySelection(start, finish)

    print("Selected Non-Overlapping Activities:")
    displayActivitiesTableFromPairs(selected)

    print("Maximum number of non-overlapping activities:", len(selected))
