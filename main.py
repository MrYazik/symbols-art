from colorama import init, Fore
from colorama import Back
from colorama import Style
import time
from modules.print_art import artText

# ToDo list:
# 1. Если потребуется, распредилить функции по модулям
# 2. Добавить выбор шрифта
# 3. Добавить выбор будут ли игнорироватся не поддерживаемые символы
# 4. Номально всё документировать

# Varibles

font = ""
chr_ignore = True

# print symbols-art


# hello massage
print('''
 ____                     _             _                           _   
/ ___|  _   _  _ __ ___  | |__    ___  | | ___          __ _  _ __ | |_ 
\___ \ | | | || '_ ` _ \ | '_ \  / _ \ | |/ __| _____  / _` || '__|| __|
 ___) || |_| || | | | | || |_) || (_) || |\__ \|_____|| (_| || |   | |_ 
|____/  \__, ||_| |_| |_||_.__/  \___/ |_||___/        \__,_||_|    \__|
        |___/                                                           
\n''')

# select language

selectLanuage = input("Select language (ru/en): ")


def questionsArtText():
    if (selectLanuage == "ru"): # Если пользыватель выбрал русский

        # Question: какой текст вывести
        printText = input("Введите текст который хотите отобразить символами (только латиские символы): ")
        print()

        # Question: how many space between characters
        printTextSpace = input("Введите пробелы между символами (по умолчанию 0): ")
        print()

        # Questiom: 
        printTextFont = input("Введите желаймый шрифт (1, 2, 3, 4, 5): ")
        print()

        artText(printText, printTextSpace, printTextFont)

    elif (selectLanuage == "en"): # Если пользыватель выбрал английский язык
        printText = input("Enter the text you want to display in symbols (Latin characters only): ")
        artText(printText, printTextSpace)

    else: # Ошибка о не коректом языке
        print()
        print(Fore.RED + "Вы ввели не коректный язык, введите \"ru\", если хотите программу на русском или \"en\", если на английском." + Style.RESET_ALL)
        return

questionsArtText()