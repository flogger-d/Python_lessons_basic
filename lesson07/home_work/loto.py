#!/usr/bin/python3
# -*- encoding utf-8 -*-

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random

def get_nums( nums ):
	while len(nums):
		idx = random.randint(0, len(nums)-1)
		yield nums.pop(idx)


# в случайном порядке выбираем бочонки с числами от 1 до 90
def get_barrels():
	return get_nums(list(range(1,91)))

# выбираем случайные 5 мест из диапазона [0, 15)
def get_placer():
	return get_nums(list(range (0,15)))
 
class Board:
	def __init__(self, name):
		self.name = name
		self.state = 'В игре'
		b = get_barrels()
		self._table = []
		for l in range(3):
			# сформируем строку из чисел
			# сначала - заготовку с пробелами
			line = [0 for i in range(15)]
			# отберем 5 чисел для строки
			nums = [b.__next__() for i in range(5)]
			nums.sort()
			# теперь - выберем 5 позиций для размещения
			p = get_placer()
			places = [p.__next__() for i in range(5)]
			places.sort()

			# теперь разместим числа по позициям
			for place,num in list(zip(places, nums)):
				line[place] = num
			# добавляем строку в карточку
			self._table.append(line)

	def print(self):
		print("{:-^45}".format(self.name)+'-')
		for row in self._table:
			line = "|"
			for col in row:
				ph = "  " if col == 0 else "--" if col == -1 else str(col)
				line += "{:2}".format(ph) + '|'
			print(line)
		print("---"*15+'-')

	def strike_out(self, num):
		for row in self._table:
			if num in row:
				row[row.index(num)] = -1
				return True
		return False

	def win(self):
		for row in self._table:
			if sum(row) != -5:
				return False
		return True

class Lotto:
	def __init__(self):
		self.player1 = Board("Ваша карточка")
		self.player2 = Board("Карточка компьютера")
		self.barrels = get_barrels()
		self.remain   = 90
	
	def Loop(self):
		while self.remain and not self.player1.win() and not self.player2.win():
			b = self.barrels.__next__()
			self.remain = self.remain-1
			print("Новый бочонок: {:2} (осталось {})".format(b, self.remain))
			self.player1.print()
			self.player2.print()
			# Действие игрока
			action = '-'
			while action not in ['y', 'n']:
				action = input("Зачеркнуть цифру? (y/n) ").lower()
			if action == 'y':
				self.player1.strike_out(b)
				self.player2.strike_out(b)


l = Lotto()
l.Loop()
			


