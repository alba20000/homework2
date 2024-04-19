print("Задание 7")
string = input("Введите строку: ").replace(" ", "")
answer = ""
for i in range(int(len(string) / 2)):
    if string[i] == string[len(string)-1-i]:
        answer = "Палиндром"
    else:
        answer = "Не палиндром"
        break
print(answer)
