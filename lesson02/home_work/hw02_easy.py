#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print("Задача #1")
fruits = ["яблоко",  "банан", "киви", "арбуз" ]

idx_max_width = math.log10(len(fruits)) if len(fruits) > 10 else 1

fruit_max_width = 0
for f in fruits:
  if fruit_max_width < len(f):
    fruit_max_width = len(f)

format_str = "{{:>{}}}. {{:>{}}}".format(idx_max_width, fruit_max_width)

i = 1;
for f in fruits:
  print(format_str.format(i, f))
  i += 1


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print("Задача #2")

list1 = [1, 5, 2, 3, 2, 4, 7, 5, 6, 7, 8, 9, 10, 7]
list2 = [2, 5, 7, 2]

print("Сначала list1 был: " + str(list1))
print("list2 был: " + str(list2))

i = 0
while i < len(list1):
  while i < len(list1) and list1[ i ] in list2:
    del list1[ i ]
  i += 1

print("После удаления элементов list2, list1 стал: " + str(list1))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print("Задача #3")

list1 = [1, 3, 4, 6, 1, 5, 10]
print("list1: " + str(list1))

list2 = []
for i in list1:
  list2.append(i*2 if i%2 else i/4)

print("list2: " + str(list2))





