Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def code(matrix, k):
    c = 0
    max_element = None
    for row in matrix:
        for elemet in row:
            if element % k == 0:
                c += 1
                if max_element is None or element > max_ekement:
                    max_element = element

                    
return c, max_element
SyntaxError: 'return' outside function
def m():
    martix = [[2,4,6],[9,12,15],[10,20,30]]
    k = 3
    c, max_element = code(matrix, k)
    print("Число элементов, кратных",k,":", c)
    print("Наибольший из этих элиментов:", max_element)
    m()