Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def code(c):
    n = 0
    while int(input()) != 0:
        n += 1
    return n
c=int(input())
r = code(c)
print(r)