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

