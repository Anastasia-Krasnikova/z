Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def min(n):
    i = 2
    while n % i != 0:
        i += 1
    return i
n = int(input())
r = min(n)
print(r)