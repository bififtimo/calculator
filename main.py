import math

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return math.trunc(x / y)

def main(str):
    try:
        arr = str.split()
        num1 = int(arr[0])
        num2 = int(arr[2])
        oper = arr[1]
        opers = ['+', '-', '*', '/']

        if len(arr) != 3 or (oper not in opers):
            raise Exception("Неверный формат строки или оператор")
        elif num1 > 10 or num1 < 1 or num2 > 10 or num2 < 1:
            raise Exception("Неверное значение чисел")

    except Exception as e:
        return e

    else:
        if oper == opers[0]:
            return addition(num1, num2)
        elif oper == opers[1]:
            return subtraction(num1, num2)
        elif oper == opers[2]:
            return multiplication(num1, num2)
        else:
            return division(num1, num2)

print("Введите выражение по шаблону: 1 + 2")
user_input = input()
result = main(user_input)

print(result)