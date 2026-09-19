import math
import cmath
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from calc.calc import Calculator

EPS = 1e-9


def approx(a, b, eps=EPS):
    if isinstance(a, complex) or isinstance(b, complex):
        eps = max(eps, 1e-4)
    return abs(a - b) < eps


def parse_res(s):
    if isinstance(s, (int, float)):
        return complex(s)
    return complex(s.replace('i', 'j'))


#1 Положительные числа
result = Calculator("4").calculate()
assert len(result) == 2
assert approx(result[0], 2.0)
assert approx(result[1], -2.0)

result = Calculator("9").calculate()
assert approx(result[0], 3.0)
assert approx(result[1], -3.0)

result = Calculator("2").calculate()
assert approx(result[0], math.sqrt(2))
assert approx(result[1], -math.sqrt(2))
print("Положительные числа - OK")


#2 Ноль
result = Calculator("0").calculate()
assert result == [0]
print("Ноль - OK")


#3 Отрицательные числа
result = Calculator("-4").calculate()
assert len(result) == 2
assert approx(parse_res(result[0]), 2j)
assert approx(parse_res(result[1]), -2j)

result = Calculator("-1").calculate()
assert approx(parse_res(result[0]), 1j)
assert approx(parse_res(result[1]), -1j)
print("Отрицательные числа - OK")


#4 Отрицательное, нечётная степень
result = Calculator("-8", pow='3').calculate()
assert len(result) == 1
assert approx(result[0], -2.0)
print("Отрицательное, нечётная степень - OK")


#5 Комплексные числа
result = Calculator("1+0i").calculate()
assert len(result) == 2
assert approx(parse_res(result[0]), 1+0j)
assert approx(parse_res(result[1]), -1+0j)

result = Calculator("0+4i").calculate()
assert approx(parse_res(result[0]), cmath.sqrt(4j))
assert approx(parse_res(result[1]), -cmath.sqrt(4j))
print("Комплексные числа - OK")


#6 Разные степени корня
result = Calculator("8", pow='3').calculate()
assert len(result) == 1
assert approx(result[0], 2.0)

result = Calculator("16", pow='4').calculate()
assert len(result) == 2
assert approx(result[0], 2.0)
assert approx(result[1], -2.0)
print("Разные степени - OK")


#7 Точность
result = Calculator("2", precision='3').calculate()
assert result[0] == round(math.sqrt(2), 3)
assert result[1] == round(-math.sqrt(2), 3)
print("Точность - OK")


#8 Некорректный ввод
assert Calculator("abc").calculate() == 'Calculation impossible!'
assert Calculator("2 + x").calculate() == 'Calculation impossible!'
print("Некорректный ввод — OK")


#9 Выражения
result = Calculator("2+2").calculate()
assert len(result) == 2
assert approx(result[0], 2.0)
assert approx(result[1], -2.0)

result = Calculator("(3+1)").calculate()
assert approx(result[0], 2.0)
print("Выражения - OK")


#10 Запятая как разделитель
result = Calculator("4,0").calculate()
assert approx(result[0], 2.0)
print("Запятая - OK")


#11 Корень первой степени
result = Calculator("5", pow='1').calculate()
assert len(result) == 1
assert approx(result[0], 5.0)
print("Корень 1-й степени - OK")


#12 Корень шестой степени
result = Calculator("64", pow='6').calculate()
assert len(result) == 2
assert approx(result[0], 2.0)
assert approx(result[1], -2.0)
print("Корень 6-й степени - OK")


#13 Комплексное число, pow=3 (три корня)
result = Calculator("1+1i", pow='3').calculate()
assert len(result) == 3
print("Комплексное pow=3 - OK")


#14 Выражение со степенью
result = Calculator("2**2").calculate()
assert len(result) == 2
assert approx(result[0], 2.0)
assert approx(result[1], -2.0)
print("Выражение со степенью - OK")


#15 Выражение с делением
result = Calculator("8/2").calculate()
assert len(result) == 2
assert approx(result[0], 2.0)
assert approx(result[1], -2.0)
print("Выражение с делением - OK")


#16 Приоритет операций
result = Calculator("2+3*4").calculate()
assert len(result) == 2
assert approx(result[0], math.sqrt(14))
assert approx(result[1], -math.sqrt(14))
print("Приоритет операций - OK")


#17 Точность 0 знаков
result = Calculator("2", precision='0').calculate()
assert result[0] == 1.0
assert result[1] == -1.0
print("Точность 0 знаков - OK")
