def square(x):
    return x * x

number = int(input("Введите целое число: "))
if number > 0:
    print("Ваше число положительное")
elif number < 0:
    print("Ваше число отрицательное")
else:
    print("Ваше число равно нулю")


if number > 0:
    total = int()
    for i in range(1, number + 1):
        total = total + i
    print(f"Сумма чисел от 1 до {number}: {total}")

print(f'Квадрат некоторых чисел: 3^2 = {square(3)}')
print(f'9^2 = {square(9)}')
print(f'(-1)^2 = {square(-1)}')