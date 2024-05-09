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
            questionsArtText()

    try: # Переводим текст в число
        printTextSpace = int(printTextSpace)
    except: # Если при этом произошла ошибка, присвоить стандартное значение
        print(Fore.RED + "Вы ввели не коректное значение. Применяется значение по умолчанию: 0" + Style.RESET_ALL)
        printTextSpace = 0

    art.tprint(printText, space = printTextSpace)
            
