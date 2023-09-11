#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

if (nr_letters <= 0 or nr_letters > len(letters)):
    print("Please enter acceptables numbers for letters.")
    exit()
if (nr_numbers <= 0 or nr_numbers > len(numbers)):
    print("Please enter accaptable numbers for numbers.")
    exit()
if (nr_symbols <= 0 or nr_symbols > len(symbols)):
    print("Please enter acceptable numbers for symbols.")
    exit()
chosen_letters = [0] * nr_letters
chosen_numbers = [0] * nr_numbers
chosen_symbols = [0] * nr_symbols
if (nr_letters == 1):
    chosen_letters[0] = letters[random.randint(0, len(letters) - 1)]
    if (nr_numbers == 1):
        chosen_numbers[0] = numbers[random.randint(0, len(numbers) - 1)]
        if (nr_symbols == 1):
            chosen_symbols[0] = symbols[random.randint(0, len(symbols) - 1)]
        else:
            for i in range(0, nr_symbols):
                chosen_symbols[i] = symbols[random.randint(
                    0,
                    len(symbols) - 1)]
    else:
        for i in range(0, nr_numbers):
            chosen_numbers[i] = numbers[random.randint(0, len(numbers) - 1)]
            if (nr_symbols == 1):
                chosen_symbols[0] = symbols[random.randint(
                    0,
                    len(symbols) - 1)]
            else:
                for i in range(0, nr_symbols):
                    chosen_symbols[i] = symbols[random.randint(
                        0,
                        len(symbols) - 1)]
else:
    for i in range(0, nr_letters):
        chosen_letters[i] = letters[random.randint(0, len(letters) - 1)]
    if (nr_numbers == 1):
        chosen_numbers[0] = numbers[random.randint(0, len(numbers) - 1)]
        if (nr_symbols == 1):
            chosen_symbols[0] = symbols[random.randint(0, len(symbols) - 1)]
        else:
            for i in range(0, nr_symbols):
                chosen_symbols[i] = symbols[random.randint(
                    0,
                    len(symbols) - 1)]
    else:
        for i in range(0, nr_numbers):
            chosen_numbers[i] = numbers[random.randint(0, len(numbers) - 1)]
            if (nr_symbols == 1):
                chosen_symbols[0] = symbols[random.randint(
                    0,
                    len(symbols) - 1)]
            else:
                for i in range(0, nr_symbols):
                    chosen_symbols[i] = symbols[random.randint(
                        0,
                        len(symbols) - 1)]
lists = chosen_letters + chosen_numbers + chosen_symbols
random.shuffle(lists)
len_list = len(lists)
print("Generated Password: ", end="")
for i in range(0, len_list):
    print(lists[i], end="")
