#Вариант 8, Костромин В.И., РИ-321055
from scipy.integrate import quad
import numpy as np
import math

#Константы по условию
a = 1
b = math.e 
Intervals = [5,10,100]

# Значение определённого интеграла
def Integrated(x):
        return x**2 + 16/x

# Метод средних прямоугольников
def MiddlePoint(n): # метод средних прямоугольников
    S = 0
    h = (b-a)/n
    for i in range(n):
        S += h * Integrated(a + h/2 + i * h)
    return S

# Метод трапеций
def Trapetions(n): # метод трапеций
    S = 0
    h = (b-a)/n
    for i in range(1, n + 1):
        S += h * (Integrated(a + (i-1)*h) + Integrated(a + i * h)) / 2
    return S

# Метод Симпсона
def Simpson(n): 
    S1 = 0
    S2 = 0
    h = (b-a)/n
    for i in range(1, n + 1, 2):
        S1 += Integrated(a + i * h)
    for i in range(2, n + 1, 2):
        S2 += Integrated(a + i * h)
    return (h/3)*(Integrated(a) + 4*S1 + 2*S2 - Integrated(b))

AnalyticValue = quad(Integrated, a, b)[0] # вычисление результата
print(f"Аналитический метод: {round(AnalyticValue, 6)}")
print(f"---------------------------------")
for n in Intervals:
    mp = MiddlePoint(n)
    print(f'Результат вычисления методом средних прямоугольников равен {mp} при n = {n}')
    print(f'Абсолютная погрешность при n = {n} для метода средних прямоугольников: {abs(mp - AnalyticValue)}')
    print(f'Относительная погрешность при n = {n} для метода средних прямоугольников: {(abs(mp - AnalyticValue) / AnalyticValue) * 100}%') 
print(f"---------------------------------")
for n in Intervals:
    trap = Trapetions(n)
    print(f'Результат вычисления методом трапеций равен {trap} при n = {n}')
    print(f'Абсолютная погрешность при n = {n} для метода трапеций: {abs(trap - AnalyticValue)}')
    print(f'Относительная погрешность при n = {n} для метода средних прямоугольников: {(abs(trap - AnalyticValue) / AnalyticValue) * 100}%')
print(f"---------------------------------")
for n in Intervals:
    simp = Simpson(n)
    print(f'Результат вычисления методом симпсона равен {simp} при n = {n}')
    print(f'Абсолютная погрешность при n = {n} для метода средних прямоугольников: {abs(simp - AnalyticValue)}')
    print(f'Относительная погрешность при n = {n} для метода средних прямоугольников: {(abs(simp - AnalyticValue) / AnalyticValue) * 100}%') 
print(f"\n")

n1 = 1
error = 100
while error >= 0.5:
  Value = MiddlePoint(n1)
  error = (abs(Value - AnalyticValue) / AnalyticValue) * 100
  if error >= 0.5:
    n1 += 1
print(f'Для метода средних прямоугольников с погрешностью не более 0.5% достаточно {n1} интервалов разбиения с погрешностью: {error}%')

n2 = 1
error = 100
while error >= 0.5:
  Value = Trapetions(n2)
  error = (abs(Value - AnalyticValue) / AnalyticValue) * 100
  if error >= 0.5:
    n2 += 1
print(f'Для метода трапеций с погрешностью не более 0.5% достаточно {n2} интервалов разбиения с погрешностью: {error}%')

n3 = 2
error = 100
while error >= 0.5:
  Value = Simpson(n3)
  error = (abs(Value - AnalyticValue) / AnalyticValue) * 100
  if error >= 0.5:
    n3 += 2
print(f'Для метода Симпсона с погрешностью не более 0.5% достаточно {n3} интервалов разбиения с погрешностью: {error}%')

#Вывод: метод Симпсона оказался наиболее точным, что доказал расчёт относительных погрешностей
