import os
import random

chars = ""
lower_chars = "abcdefghijklnopqrstuvwxyz"
upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number_chars = "1234567890"
spec_chars = "+-/*!&$#?=@<>"

print("[1] - Да, [2]-Нет")
print()
upper_chars_select = int(input("Заглавные буквы: "))
lower_chars_select = int(input("Строчные буквы: "))
number_chars_select = int(input("Цифры: "))
spec_chars_select = int(input("Специальные символы: "))
print()
passwords_amount = int(input("Кол-во паролей: "))
password_length = int(input("Длина пароля: "))

if upper_chars_select == 1:
    chars = chars + upper_chars
if lower_chars_select == 1:
    chars = chars + lower_chars
if spec_chars_select == 1:
    chars = chars + spec_chars
if number_chars_select == 1:
    chars = chars + number_chars

for x in range(passwords_amount):
    password = ""
    for i in range(password_length):
        password += random.choice(chars)

    file = open("Pass.txt", "a")
    file.write(password + "\n")
    file.close()
print("Пароли сгенерированы")
file = open("Pass.txt", "r")
print("".join(file.readlines()) + "\n")
file.close()
os.remove(f"C:/Users/timof/PycharmProjects/SimplePasswordGenerator/Pass.txt")
