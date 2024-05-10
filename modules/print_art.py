from colorama import init, Fore
from colorama import Back
from colorama import Style
import art

# Получить названия шрифтов можно при помощи сайта: https://www.fontcopypaste.com/


# Основная функция 

def artText(printText, printTextSpace, printTextFont): # Отрисовка текста и обработка ошибок

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
            questionsArtText()
    
    # Вывод шрифта 
    if (printTextFont == "1"):
        printTextFont = 'DEFAULT_FONT'
    elif (printTextFont == "2"):
        printTextFont = 'block'
    elif (printTextFont == "3"): 
        printTextFont = 'small'
    elif (printTextFont == "4"): 
        printTextFont = 'fancy5'
    elif (printTextFont == "5"): 
        printTextFont = 'small'
    else:
        print(Fore.RED + "Вы ввели не коректное значение в вопросе о шрифте. Применяется значение по умолчанию: DEFAULT_FONT" + Style.RESET_ALL)
        printTextFont = 'DEFAULT_FONT'

    # Перевод текста в число (для printTextSpace)
    
    try: # Переводим текст в число
        printTextSpace = int(printTextSpace)
    except: # Если при этом произошла ошибка, присвоить стандартное значение
        print(Fore.RED + "Вы ввели не коректное значение в вопросе о количестве пробелов. Применяется значение по умолчанию: 0" + Style.RESET_ALL)
        print()
        printTextSpace = 0

    art.tprint(printText, space = printTextSpace, font=printTextFont) # Вызов основной функции
            