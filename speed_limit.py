list_of_speeds_sets = []

def travelled(speeds: list) -> str:
    current_distance = 0
    current_time = 0
    for speed, time in speeds:
        current_distance += speed * (time - current_time)
        current_time = time
    return f"{current_distance} miles"

while True:
    set_size = int(input())
    if set_size == -1:
        break
    else:
        current_set_of_speeds = []
        for _ in range(set_size):
            input_str = input()
            speed_tuple = tuple(map(int, input_str.split(" ")))
            current_set_of_speeds.append(speed_tuple)
        list_of_speeds_sets.append(current_set_of_speeds)

for speeds_set in list_of_speeds_sets:
    print(travelled(speeds_set))

