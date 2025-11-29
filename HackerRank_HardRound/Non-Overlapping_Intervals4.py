n = int(input("Enter the number: "))
intervals = []
for i in range(n):
    x,y = map(int,input().split())
    intervals.append([x,y])
if len(intervals) == 1:
    print(intervals)
else:
    intervals.sort()
    toRemove = 0
    prev_end = intervals[0][1]
    for i in range(1,len(intervals)):
        start,end = intervals[i]
        if prev_end < start:
            toRemove += 1
            prev_end = min(prev_end,end)
        else:
            prev_end = end

print(toRemove)