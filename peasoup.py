# accept user inputs and create a dict
menu_items = []
restaurant = {}  # dict
n = int(input())  # number of restaurants

for _ in range(n):
    k = int(input())  # number of items on the menu
    restaurant_name = input().strip().lower()

    for item in range(k): # add each menu item into a list
        menu_items.append(input().strip().lower())

    restaurant[restaurant_name] = menu_items
    menu_items = []

for restaurant_name, menu in restaurant.items():
    if "pea soup" in menu and "pancakes" in menu:
        print(str(restaurant_name))
        break

    print("Anywhere is fine I guess")


