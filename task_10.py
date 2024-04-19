print("Задание 10")
string = input("Введите строку: ")
reversed_list = []
for i in range(len(string)):
    reversed_list.append(string[len(string)-1-i])
reversed_string = "".join(reversed_list)
print(reversed_string)
