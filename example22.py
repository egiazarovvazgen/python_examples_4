"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
"""

molFirst = [int(x) for x in input("Введите количество элементов первого множества: ").split()]
molSecond = [int(x) for x in input("Введите количество элементов второго множества: ").split()]
n = molFirst[0]
m = molSecond[0]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input("Введите элементы первого множества: ").split()]
k = set(a)
for i in k:
    set_1.add(i)
b = [int(x) for x in input("Введите элементы второго множества: ").split()]
k1 = set(b)
for i in k1:
    set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
print("Числа, которые встречаются в обоих наборах, расположенные в порядке возрастания: ")
for i in kool:
    print(i, end=' ')
