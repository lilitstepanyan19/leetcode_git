def canAttendMeeting(intervals):
    intervals.sort()

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True

print(canAttendMeeting([[0,30], [5,10],[15,20]]))
print(canAttendMeeting([[7,10], [2,4]]))
print(canAttendMeeting([[7,13], [13,15]]))