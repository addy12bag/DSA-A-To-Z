def merger_intervals(intervals):
    if not intervals:
        return []
    intervals.sort()
    res = [intervals[0]]

    for i in range(1,len(intervals)):
        last = res[-1]
        curr = intervals[i]

        if curr[0]<=last[1]:
            last[1] = max(last[1],curr[1])
        else: res.append(curr)
    return res

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(merger_intervals(intervals))