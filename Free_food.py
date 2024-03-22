N = int(input()) # number of events

days = set()
for _ in range(N):
    s, t = map(int, input().split())
    for i in range(s-1, t+1):
        days.add(i)

print(len(days))