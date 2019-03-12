#!/usr/bin/python3
# enconding utf-8

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import os
import sys

from .hw05_easy import ls_func


Run = True

def Pwd():
     print("Текущий каталог: "+os.getcwd())

def Cd():
     path = input("Куда перейти: ")
     try:
          os.chdir(path)
          print("Ok")
     except Exception as e:
          print("Ошибка: " + str(e))

def Ls():
     print("======ТЕКУЩИЙ КАТАЛОГ===")
     hw05_easy.ls_func()
     print("======КОНЕЦ=============")

def MkDir():
     path = input("Создать каталог. Введите имя каталога: ")
     try:
          os.mkdirs(path)
          print("Ok")
     except Exception as e:
          print("Ошибка создания каталога: "+str(e))

def RmDir():
     path = input("Удалить каталог. Введите имя каталога: ")
     try:
          os.rmdir(path)
          print("Ok")
     except Exception as e:
          print("Ошибка удаления каталога: "+str(e))

def Exit():
     print("До свидания!")
     global Run
     Run = False

text = [
     "Текущий каталог",
     "Перейти в новый каталог",
     "Содержимое текущего каталога",
     "Создать каталог",
     "Удалить каталог (должен быть пустым!)",
     "Выход из программы"
]

handlers = [
     Pwd,
     Cd,
     Ls,
     MkDir,
     RmDir,
     Exit
]


commands = [[i, t, h] for i, t, h in zip(range(1,len(text)+1), text, handlers) ]

def REPL():
     print("Вам доступны следующие действия: ")
     for  i,t,_  in commands:
          print("{}. {}".format(i,t))
     try:
          i = int(input("Введите индекс команды: "))
          if i in range(1,len(commands)+1):
               print("\n\n{}:\n".format(commands[i-1][1]))
               commands[i-1][2]()
               print("\n")
          else:
               print("'"+i+"': Команда не найдена!")
     except Exception as e:
          print("Ошибка: "+str(e))
          print("Нужно ввести число из указанного диапазона")

if __name__ == "__main__":
     while Run:
          REPL()


