import numbers


def check_input(inputed):
    is_correct = False
    while not is_correct:
        try:
            number = float(input(f"{inputed}"))
            is_correct = True
        except ValueError:
            print("That is not number")
    return number


def convert_to_list(n):
    if n < 0:
        n = n * - 1
    temp_int = str(n)
    temp_int = temp_int.translate({ord('.'): None})
    new_list = list(temp_int)
    return new_list


def find_sum(arr):
    result = 0
    for n in range(0, len(arr)):
        result += int(arr[n])
    print(result)


num = check_input('enter the number: ')
find_sum(convert_to_list(num))