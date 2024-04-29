import art
from colorama import init, Fore
from colorama import Back
from colorama import Style
import time

# ToDo list:
# 1. Если потребуется, распредилить функции по модулям
# 2. Добавить выбор шрифта
# 3. Добавить выбор будут ли игнорироватся не поддерживаемые символы
# 4. Номально всё документировать

# Varibles

font = ""
chr_ignore = True

# print symbols-art

def artText(printText, printTextSpace): # Отрисовка текста и обработка ошибок

    # Проверка на введён ли текст?
    if (printText == ""):
        if (selectLanuage == "ru"):
            print()
            print(Fore.RED + "Вы не ввели текст который хотите нарисовать" + Style.RESET_ALL)
            print()
            questionsArtText()
        elif (selectLanuage == "en"):
            print()
            print(Fore.RED + "You have not entered the text you want to draw" + Style.RESET_ALL)
            print()

    try: # Переводим текст в число
        printTextSpace = int(printTextSpace)
    except: # Если при этом произошла ошибка, присвоить стандартное значение
        print(Fore.RED + "Вы ввели не коректное значение. Применяется значение по умолчанию: 0" + Style.RESET_ALL)
        printTextSpace = 0

    art.tprint(printText, space = printTextSpace)
            

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
    if (selectLanuage == "ru"):

        # Question: why text output?
        printText = input("Введите текст который хотите отобразить символами (только латиские символы): ")
        print()

        # Question: how many space between characters
        printTextSpace = input("Введите пробелы между символами (по умолчанию 0): ")
        print()

        artText(printText, printTextSpace)
    elif (selectLanuage == "en"):
        printText = input("Enter the text you want to display in symbols (Latin characters only): ")
        artText(printText, printTextSpace)
    else:
        print()
        print(Fore.RED + "Вы ввели не коректный язык, введите \"ru\", если хотите программу на русском или \"en\", если на английском." + Style.RESET_ALL)
        return

questionsArtText()