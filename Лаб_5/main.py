data = [
    326, 4055, 9224, 1812, 2762,
    -2536, -9978, 2299, -2775, -1363,
    2265, 1730, 4522, -9583, -58,
    -8456, -3559, -1275, -6333, 4341,
]

sra = sum(data) / len(data)
print(len(data))
print(data)
print(sra)

counter = 0
max_sum = int()

for i in range(len(data) - 1):
    x, y = data[i], data[i + 1]
    if (x > sra or y > sra) and (x % 17 == 0 or y % 17 == 0):
        counter += 1
        max_sum = max(max_sum, x + y)

print(f"Количество подходящих пар = {counter}")
print(f"Максимальная сумма = {max_sum}")
