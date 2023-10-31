Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def code():
    n = int(input())
    c = 0
    max_c = 0
    p = n
    while n != 0:
        if n == p:
            c += 1
            if c > max_c:
                max_c = c
        else:
            c = 1
        p = n
        n = int(input())
    return max_c
r = code()
print(r)