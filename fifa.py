n = int(input("How many improvemnts? "))
k = int(input("How many improvements per year? "))

def what_year(n: int, k: int) -> int:
    return round((n / k)) + 2022

print(what_year(n,k))