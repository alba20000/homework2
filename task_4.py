print("Задание 4")
my_list = ["Abraham", "Josef", "Mark",
           "Kelly", "Bob", "Jules",
           "Cathy", "Dolores", "Nigel"]
enum_list = enumerate(my_list, 1)
for name in enum_list:
    if name[0] % 3 == 0:
        print(name)
