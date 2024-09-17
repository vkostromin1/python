#Вариант 8, Костромин В.И., РИ-321055
from scipy.integrate import quad
import numpy as np
import math

#Константы по условию
a = 1
b = math.e 
Intervals = [5,10,100]
Methods = ["MiddlePoint", "Trapetions", "Simpson"]

class IntegralValue:
    # Значение определённого интеграла
    def Integrated(integral, x):
        return x**2 + 16/x
    # Функция инициализации свойства объекта integral
    def __init__(integral, a , b) -> None:
        integral.MethodsNames = [integral.MiddlePoint , integral.Trapetions, integral.Simpson]
        integral.FirstValue = a
        integral.EndValue = b
        integral.Calculate()
    # Аналитический метод (1 задание)
    def Analytic(integral): 
        return quad(integral.Integrated, integral.FirstValue, integral.EndValue)[0]
    # Метод средних прямоугольников
    def MiddlePoint(integral, n): 
        h2 = 0
        h = (integral.EndValue - integral.FirstValue)/ n
        for i in range(0, n-1):
            h2 = h2 + h * integral.Integrated(integral.FirstValue + h/2 + i * h)
        return h2
    # Метод трапеций
    def Trapetions(integral, n):
        h = (integral.EndValue - integral.FirstValue)/n 
        h2 = h*(integral.Integrated(integral.FirstValue) + integral.Integrated(integral.EndValue))/ 2
        for i in range(1, n -1):
            h2 = h2 + h * integral.Integrated(integral.FirstValue + i * h)
        return h2
    # метод Симпсона
    def Simpson(integral, n):
        h = (integral.EndValue-integral.FirstValue)/(2 * n)
        h1 = 0
        h2 = 0
        for i in range(1 , n):
            x1 = integral.FirstValue + (2*i - 1) * h
            h1 = h1 + integral.Integrated(x1)
            x2 = x1 + h 
            h2 = h2 + integral.Integrated(x2)
        h3 = h/3*(integral.Integrated(integral.FirstValue) + 4* h1 + 2 * h2 - integral.Integrated(integral.EndValue))
        return h3
    # Вычисление численно по методам и определение абсолютных погрешностей (2-3 задание)
    def Calculate(integral):
        integral.AnalyticValue = integral.Analytic()
        print(f"Analitic Method: {round(integral.AnalyticValue, 6)}")
        for i in range(len(Intervals)):
            MidIntegralValue = integral.MethodsNames[0](Intervals[i])
            Accuracy = abs(integral.AnalyticValue - MidIntegralValue)
            print (f"Method {Methods[0]}, n = {Intervals[i]} :  {MidIntegralValue} with accuracy : {round(Accuracy,6)} ")
        for i in range(len(Intervals)):
            TraIntegralValue = integral.MethodsNames[1](Intervals[i])
            Accuracy = abs(integral.AnalyticValue - TraIntegralValue)
            print (f"Method {Methods[1]}, n = {Intervals[i]} :  {TraIntegralValue} with accuracy : {round(Accuracy,6)} ")
        for i in range(len(Intervals)):
            SimIntegralValue = integral.MethodsNames[2](Intervals[i])
            Accuracy = abs(integral.AnalyticValue - SimIntegralValue)
            print (f"Method {Methods[2]}, n = {Intervals[i]} :  {SimIntegralValue} with accuracy : {round(Accuracy,6)} ")

IntegralValue(a,b)


