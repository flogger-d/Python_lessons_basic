#!/usr/bin/python3
# encoding utf-8


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

if __name__ == "__main__":
     import os
     import sys

def ls_func():
     try:
          for root, dirs, files in os.walk('.'):

               for d in dirs.sort():
                    print(" {}".format(d))

               for d in files.sort():
                    print(" {}".format(d))

     except Exception as e:
          print('Ошибка: '+str(e))

def ls_dirs_func():
     try:
          for root, dirs, files in os.walk('.'):
               for d in dirs:
                    print(" - {}".format(d))
     except Exception as e:
          print('Ошибка: '+str(e))

if __name__ == "__main__":
     print("Задача #1")
     try:
          input('Создадим папки dir_1 - dir_9 в текущем каталоге')
          path = os.getcwd()
          mkdirs = [os.path.join(path,'dir_'+str(d)) for d in range(10)]
          for d in mkdirs:
               if not os.path.exists(d):
                    os.mkdir(d)

          ls_dirs_func()

          input('А теперь удалим их')

          for d in mkdirs:
               os.rmdir(d)

          ls_dirs_func()

     except Exception as e:
          print("Ошибка: " + str(e))


     # Задача-2:
     # Напишите скрипт, отображающий папки текущей директории.

     print("Задача #2")
     input("В текущей директории есть следующие папки:")
     ls_dirs_func()


     # Задача-3:
     # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

     print("Задача #3")

     myself = sys.argv[0]
     print("Скрипт запущен из файла '"+myself+"'")

     myself_copy = myself+".copy"
     print("Файл будет скопирован в '"+myself_copy+"'")

     os.system('cp ' + myself + ' ' + myself_copy)



