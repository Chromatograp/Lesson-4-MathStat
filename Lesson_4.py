# -*- coding: utf-8 -*-
"""Копия 2.3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ckpt4Wdw_gzuF8bpy46rIZ-2QijoOxzY
"""

from math import factorial
import numpy as np
import math
import statistics

print('Задание 1.')

# Случайная непрерывная величина A имеет равномерное распределение на промежутке
# (200, 800].
# Найдите ее среднее значение и дисперсию.

A = [200, 800]

M = statistics.mean(A)

D = statistics.variance(A)

print('Выборка:', A)
print('Среднее значение:', M)
print('Дисперсия:', D)

print('Задание 2.')

# О случайной непрерывной равномерно распределенной величине B известно, что ее
# дисперсия равна 0.2. Можно ли найти правую границу величины B и ее среднее
# значение зная, что левая граница равна 0.5?
# Если да, найдите ее.

# Находим правую границу величины В, выразив ее через формулу вычисления дисперсии:

def B(d, a):
  b = np.sqrt(d * 12) + a
  return b

# Вычисляем среднее значение с использованием полученной величины:

def M(B, a):
  m = (a + B) / 2
  return m

b = B(0.2, 0.5)

print('Правая граница случайной величины В:', "{:.3f}".format(b))
print('Среднее значение:', "{:.3f}".format(M(b, 0.5)))

print('Задание 3.')

# Непрерывная случайная величина X распределена нормально и задана плотностью
# распределения
# f(x) = (1 / (4 * sqrt(2*pi))) * (exp(-(x+2)**2) / 32).
# Найдите:
# а). M(X)
# б). D(X)
# в). std(X) (среднее квадратичное отклонение)

# Согласно формуле плотности распределения:

M = 2

D = 32 / 2

std = np.sqrt(16)

print('Среднее значение:', M)
print('Дисперсия:', D)
print('Среднее квадратичное отклонение:', std)

print('Задание 4.')

# Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см
# б). больше 190 см
# в). от 166 см до 190 см
# г). от 166 см до 182 см
# д). от 158 см до 190 см
# е). не выше 150 см или не ниже 190 см
# ё). не выше 150 см или не ниже 198 см
# ж). ниже 166 см.

# Во всех случаях, где вопрос стоит только о правой или левой стороне выборки,
# ответ можно вычислить как половину от разницы общей вероятности и соответствующей
# сигма:

def people(m, std, b, sigma_1, sigma_2, sigma_3):
  p = []
  sigma = b - m
  if sigma == std:
    p = (1 - sigma_1) / 2
  elif sigma == std * 2:
    p = (1 - sigma_2) / 2
  elif sigma < 0:
    p = (1 - sigma_1) / 2
  else:
    pass
  return p

# В остальных случаях ответ равен либо самой доле от выборки, либо разницы доли
# от выборки и общей вероятности:

def people_2(m, std, a, b, sigma_1, sigma_2, sigma_3):
  p = []
  sigma_ = a - m
  sigma = b - m
  if sigma == std and sigma_ == -(std):
    p = sigma_1
  elif sigma == std * 2 and sigma_ == -(std * 2):
    p = sigma_2
  elif sigma == std * 3 and sigma_ == -(std * 3):
    p = 1 - sigma_3
  elif sigma == std * 2 and sigma_ == -(std):
    p = sigma_1 + (sigma_2 - sigma_1) / 2
  elif sigma == std * 2 and sigma_ == -(std * 3):
    p = 1 - (sigma_2 + (sigma_3 - sigma_2) / 2)
  else:
    pass
  return p

print('Вероятность того, что случайный человек из выборки окажется выше 182 см:', "{:.2f}".format(people(174, 8, 182, 0.68, 0.954, 0.9972)))
print('Вероятность того, что случайный человек из выборки окажется выше 190 см:', "{:.3f}".format(people(174, 8, 190, 0.68, 0.954, 0.9972)))
print('Вероятность того, что случайный человек из выборки попадет в диапазон 166-190 см:', "{:.3f}".format(people_2(174, 8, 166, 190, 0.68, 0.954, 0.9972)))
print('Вероятность того, что случайный человек из выборки попадет в диапазон 166-182 см:', "{:.3f}".format(people_2(174, 8, 166, 182, 0.68, 0.954, 0.9972)))
print('Вероятность того, что случайный человек из выборки попадет в диапазон 158-190 см:', "{:.3f}".format(people_2(174, 8, 158, 190, 0.68, 0.954, 0.9972)))
print('Вероятность того, что случайный человек из выборки окажется не выше 150 см или не ниже 190 см:', "{:.3f}".format(people_2(174, 8, 150, 190, 0.68, 0.954, 0.9972)))
print('Вероятность того, что случайный человек из выборки окажется не выше 150 см или не ниже 198 см:', "{:.4f}".format(people_2(174, 8, 150, 198, 0.68, 0.954, 0.9972)))
print('Вероятность того, что случайный человек из выборки окажется ниже 166 см:', "{:.2f}".format(people(174, 8, 166, 0.68, 0.954, 0.9972)))

print('Задание 5.')

# На сколько сигм (средних квадратичных отклонений) отклоняется рост человека,
# равный 190 см, от математического ожидания роста в популяции, в которой
# M(X) = 178 см и D(X) = 25 кв.см?

def sigma(m, d, x):
  std = np.sqrt(d)
  s = (x - m) / std
  return s

print(f'Рост человека 190 см отклоняется от среднего значения данной выборки на {sigma(178, 25, 190)} сигмы')