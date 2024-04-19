print("Задание 2")
max_word_length = 0
max_word = ""
word_list = ["apple", "pear", "banana", "kiwi"]

for word in word_list:
    if len(word) > max_word_length:
        max_word_length = len(word)
        max_word = word
print(max_word)

max_word_length = 0
max_word = ""

iterator = iter(word_list)
try:
    while True:
        next_word = next(iterator)
        if len(next_word) > max_word_length:
            max_word_length = len(next_word)
            max_word = next_word
except StopIteration:
    print(max_word)
