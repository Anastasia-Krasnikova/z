# -- coding: utf-8 —
a = b =1 
N = int(input())-2
print(a,b,end = ' ')
for i in range(2,N):
    a,b = b, a +b
    print(b,end = ' ')
