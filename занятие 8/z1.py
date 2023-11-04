
def funkzia(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
def prozeduura(n):
    count = 0
    while n > 0:
        n -= funkzia(n)
        count += 1
    return count
number = 23
d = prozedura(number)
print(f"Через {d} действий получится ноль")
