Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def code():
    s = str(input("Введите строку: "))
    word = str(input("Введите слово: "))
    count = s.lower().count(word.lower())
    print(f"Слово '{word}' встречается {count} раз(а) в тексте.")
    r=code()
    print(r)