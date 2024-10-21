with open('text.txt', 'r') as file: #Открываем файл text.txt
        content = file.read() #Читаем файл
        words = content.split() #Находим кол-во слов
        print("В вашем файле находится " + str(len(words)) + " слов") #Выводим кол-во слов