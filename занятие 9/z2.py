import numpy as np
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
    return np.delete(np.delete(matrix, r, axis=0), c, axis=1)
n = 4
matrix = np.random.randint(-10, 10, size=(n, n))
print("Исходная матрица:")
print(matrix)
l_v, l_r, l_c = code(matrix)
print("Наибольший по модулю элемент:", l_v)
new_matrix = m(matrix, l_r, l_c)
print("Новая матррица:")
print(new_matrix)
