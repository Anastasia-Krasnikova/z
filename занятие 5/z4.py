Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def dni(x, y):
    c = 1
    while x < y:
        x *= 1.1
        c += 1
    return c
x=int(input())
y=int(input())
r=dni(x, y)
print(r)