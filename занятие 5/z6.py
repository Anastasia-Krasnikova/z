Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def code(k):
    sum = 0
    n = int(input())
    c = 0
    while n != 0:
        sum += n
        c += 1
        n = int(input())
    return sum / c
k=int(input())
r = code(k)
print(r)