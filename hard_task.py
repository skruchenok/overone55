def comp(num1, num2):
    if (type(num1) == int or type(num1) == float) and (type(num2) == int or type(num2) == float):
        if num1 > num2:
            return num1
        elif num1 < num2:
            return num2
        else:
            return num1
    else:
        raise ValueError("Некоректные числа для сравнения")


def edit(num, day, k):
    if (type(num) == int or type(num) == float) and type(day) == int:
        while day:
            num *= k
            day -= 1
    else:
        raise ValueError("Введены некорректные числа")
    return num


# try:
#     print(edit('1', 30, 2))
# except ValueError as e:
#     print(e)
