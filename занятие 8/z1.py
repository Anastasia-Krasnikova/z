Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def funkzia(n):
    s += n % 10
    n //= 10
    return s
def prozeduura(n):
    
SyntaxError: invalid syntax
count = 0
while n > 0:
    n -= funkzia(n)
    count += 1
    return count
SyntaxError: 'return' outside function
number = 23
d = prozedura(number)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d = prozedura(number)
NameError: name 'prozedura' is not defined
drint(f"Через {d} действий получится ноль")