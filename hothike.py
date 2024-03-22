# initialise variables
n = int(input())
t = list(map(int, input().split()))
best_start_day = 1
min_max_temp = max(t[0], t[2])

for i in range(n-2):
    compare = max(t[i], t[i+2])
    if compare < min_max_temp:
        min_max_temp = compare
        best_start_day = i+1
print(best_start_day, min_max_temp)

