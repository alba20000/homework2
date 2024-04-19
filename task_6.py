print("Задание 6")
digit = input("Введите число: ")
m = int(digit.replace("-",""))
n = m
digit_count = 0
for i in range(len(str(n))):
    m = m // 10
    digit_count += 1
print(digit_count)

digit_count = 0
if n == 0:
    digit_count = 1
else:
    while n > 0:
        n = n // 10
        digit_count += 1
print(digit_count)
