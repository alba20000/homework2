print("Задание 9")
my_list = [1, 1, 1, 2, 2, 3, 4]
print(my_list)
answer = ""
for el in my_list:
    if my_list.count(el) > 1:
        del my_list[el]
print(my_list)

my_list = [1, 1, 1, 2, 2, 3, 4]
iterator = iter(my_list)
try:
    while True:
        el = next(iterator)
        if my_list.count(el) > 1:
            del my_list[el]
except StopIteration:
    print(my_list)
