def p(massif):
    pr = 1
    for num in massif:
        pr *= num
    return pr
def a(massif):
    sum = 0
    for num in massif:
        sum += num
    return sum / len(massif)
    massif1 = [2,4,6,8]
    massif2 = [1,3,5,7]
    massif3 = [10,20,30,40]
    pr1 = p(massif1)
    pr2 = p(massif2)
    pr3 = p(massif3)
    a1 = a(massif1)
    a2 = a(massif2)
    a3 = a(massif3)
    print("Pr of massif1:", pr1)
    print("Pr of massif2:", pr2)
    print("Pr of massif3:", pr3)
    print("A of massif1:", a1)
    print("A of massif2:", a2)
    print("A of massif3:", a3)
