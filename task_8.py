print("Задание 8")
my_list = [1, 5, 2, 5, 3, 4]
answer = ""
for el in my_list:
    if my_list.count(el) > 1:
        answer = "Есть дубликаты"
        break
    else:
        answer = "Нет дубликатов"
print(answer)
