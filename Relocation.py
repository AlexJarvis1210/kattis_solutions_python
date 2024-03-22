N, Q = map(int, input("").split())

# Take the user input of company locations and create a list of companies. The index of the list will order the companies
companies = [int(number) for number in input("").split()]

# Create a directory dict with company number as the key (the company number is index+1 of companies[]), and company location as the value taken from the list.
directory = {}
for index, company in enumerate(companies):
    directory[index+1]= company

# process the Q orders
query = []
for _ in range(Q):
    # create a list of the orders, converted from inputted string into integers
    orders = [int(number) for number in input("").split()]
    if orders[0] == 1:
        directory[orders[1]] = orders[2]
    else:
        # Append the list with the absolute distance between two companies. Using abs() ensures
        # that the result is always a positive integer, representing the non-negative nature of distance
        query.append(abs(directory[orders[1]] - directory[orders[2]]))

for distance in query:
    print(distance)