name = str(input(""))
a = int(input(""))
b = int(input(""))
ans = int(input(""))


def is_sith_or_jedi(x: int, y: int, answer: int) -> str:
    if 0 < x - y == answer:
        return "VEIT EKKI"
    elif answer == abs(x - y):
        return "SITH"
    else:
        return "JEDI"


print(is_sith_or_jedi(a, b, ans))
