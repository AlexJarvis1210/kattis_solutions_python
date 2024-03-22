numbers = []
for _ in range(10):
    numbers.append(int(input()))


def modulo(list_of_numbers: list) -> int:
    set_of_modulo = set()
    for i in range(0, len(list_of_numbers)):
        set_of_modulo.add(list_of_numbers[i] % 42)
    return len(set_of_modulo)


print(modulo(numbers))
