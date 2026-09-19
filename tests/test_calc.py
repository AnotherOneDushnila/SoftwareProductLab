import math
import cmath
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from calc.calc import Calculator

EPS = 1e-9

def approx(a, b, eps=EPS):
    return abs(a - b) < eps

# Статусы
assert Calculator("4").status == 'positive'
assert Calculator("0").status == 'positive'
assert Calculator("-4").status == 'negative'
assert Calculator("1+2i").status == 'complex'
assert Calculator("3j").status == 'complex'
print("Статусы прошли тест")

# Положительные числа
result = Calculator("4").calculate()
assert len(result) == 2
assert result[0] == 2
assert result[1] == -2

result = Calculator("9").calculate()
assert result[0] == 3
assert result[1] == -3

result = Calculator("0").calculate()
assert result[0] == 0
assert result[1] == 0

result = Calculator("2").calculate()
assert result[0] == math.sqrt(2)
assert result[1] == -math.sqrt(2)
print("Положительные числа прошли тест")

# Отрицательные числа
result = Calculator("-4").calculate()
assert approx(result[0],  2j)
assert approx(result[1], -2j)

result = Calculator("-1").calculate()
assert approx(result[0],  1j)
assert approx(result[1], -1j)
print("Отрицательные числа прошли тест")

# Комплексные числа
result = Calculator("1+0i").calculate()
assert len(result) == 2
assert approx(result[0],  1+0j)
assert approx(result[1], -1+0j)

result = Calculator("0+4i").calculate()
assert approx(result[0],  cmath.sqrt(4j))
assert approx(result[1], -cmath.sqrt(4j))
print("Комплексные числа прошли тест")
