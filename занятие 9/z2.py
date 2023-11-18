Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
def code(matrix):
    max_abs_v = 0
    max_abs_r = 0
    max_abs_c = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            abs_v = abs(matrix[i][j])
            if abs_v > max_abs_v:
                max_abs_v = abs_v
                max_abs_r = i
                max_abs_c = j
    return max_abs_v, max_abs_r, max_abs_c
def m(matrix, r, c):
    
SyntaxError: invalid syntax
return np.delete(np.delete(matrix, r, axis=0), c, axis=1)
SyntaxError: 'return' outside function
n=4
matrix = np.random.randint(-10, 10, size=(n,n))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    matrix = np.random.randint(-10, 10, size=(n,n))
NameError: name 'np' is not defined. Did you mean: 'n'?
print("Исходная матрица:")
Исходная матрица:
print(matrix)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(matrix)
NameError: name 'matrix' is not defined
new_matrix = m(matrix, l_r, l_c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    new_matrix = m(matrix, l_r, l_c)
NameError: name 'm' is not defined
print("Новая матррица:")
Новая матррица:
print(new_matrix)