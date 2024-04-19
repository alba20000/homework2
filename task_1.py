print("Задание 1")
n = int(input("Введите n: "))
result = 0
for i in range(n+1):
    if i % 2 == 0:
        result += i
print(result)

result2 = 0
j = 0
while j <= n:
    if j % 2 == 0:
        result2 += j
    j += 1
print(result2)
