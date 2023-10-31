Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def code(A, B) :
    print ("Исходный массив А:", А)
    print("Исходный массив В:", B)
    А, В = В, А
    print("Преобразованный массив A:", A)
    print("Преобразованный массив В:", В)
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 101
B = [11, 12, 13, 14, 15, 16, 17, 18, 19, 201
r=code (A, B)
print(r)