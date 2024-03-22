shops_to_visit = []
trips = []
iterations = int(input())  # number of parses

for _ in range(iterations):
    number_of_shops = int(input())
    shop_list = list(map(int, input().split(" ")))
    shops_to_visit.append(shop_list)

for i in range(0, len(shops_to_visit)):
    running_total = 0
    low = min(shops_to_visit[i])
    high = max(shops_to_visit[i])
    parking_space = (high + low) // 2
    running_total += parking_space - low
    running_total += high - low
    running_total += high - parking_space
    trips.append(running_total)

for trip in trips:
    print(trip)
