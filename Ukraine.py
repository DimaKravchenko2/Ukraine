def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Выберете действие:")
print("1.Добавить")
print("2.Вычесть")
print("3.Умножить")
print("4.Разделить")

while True:
    choice = input("Введите число(1/2/3/4): ")


    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Введите первое число:: "))
        num2 = float(input("Введите второе число: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_calculation = input("Давайте сделаем следующий расчет? (да, нет): ")
        if next_calculation == "нет":
            break

    else:
        print("Неверный ввод")