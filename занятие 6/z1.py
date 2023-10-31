def code():
    s = str(input("Введите строку: "))
    word = str(input("Введите слово: "))
    count = s.lower().count(word.lower())
    print(f"Слово '{word}' встречается {count} раз(а) в тексте.")
    r=code()
    print(r)
