def check_input(inputed):
    is_correct = False
    while not is_correct:
        try:
            number = int(input(f"{inputed}"))
            is_correct = True
        except ValueError:
            print("uncorrectable")
    return number


def without_factorial(num):
    if num == 1:
        return 1
    else:
        return num * without_factorial(num - 1)


def add_in_list(number):
    list = []
    for i in range(1, num + 1):
        list.append(without_factorial(i))
    print(f"multiplication from 1 to {num}: {list}")


num = check_input('enter the number: ')
number = num

add_in_list(without_factorial(num))
