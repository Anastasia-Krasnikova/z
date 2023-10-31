def code(a):
    min_abs = min(a, key=abs)
    r_a = [al::-1]
    return min_abs, r_a
а = input("Введите элементы массива через пробел: ").split()
a = [float(x) for x in a]
result_min, result_r = code(a)
print ("Минимальный по модулю элемент: ", result_min)
print("Массив в обратном порядке: ", result_r)
