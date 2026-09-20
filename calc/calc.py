from math import cos, sin, pi
from cmath import phase
from sympy import I, zoo, nan
from sympy.core.sympify import *
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor
import re
from typing import Any


transformations = standard_transformations + (implicit_multiplication_application, convert_xor)


class Calculator:

    def __init__(self, input: str, pow: str = '2', precision: str = '10') -> None:
        self.input = input.strip()
        try:
            self.precision = int(precision)
        except (ValueError, TypeError):
            raise ValueError('Precision must be an integer!')
        
        if self.precision < 0:
            raise ValueError('Precision must be an integer >= 0!')

        
        try:
            self.pow = int(pow)
        except (ValueError, TypeError):
            raise ValueError('Precision must be an integer!')
        
        if self.pow <= 0:
            raise ValueError('Root degree must be > 0!')


    def calculate(self) -> list:
        num = self._parse_exp()

        if num is None:
            return 'Calculation impossible!'
        elif type(num) == complex:
            return self._complex_root(num, self.pow)
        elif num < 0:
            return self._negative_root(num, self.pow)
        elif num > 0:
            return self._basic_root(num, self.pow)
        elif num == 0:
            return [0]
        else:
            raise ValueError()


    def _basic_root(self, input: float, pow: int = 2) -> list[float]:
        basic_root = round(input ** (1/pow), self.precision)

        if pow % 2 == 0:
            return [basic_root, -basic_root]
        return [basic_root]


    def _negative_root(self, input: float, pow: int = 2) -> list:
        if pow % 2 == 0:
            return self._complex_root(complex(input), pow)
        return [round(-((-input) ** (1 / pow)), self.precision)]


    def _complex_root(self, input: complex, pow: int = 2) -> list[str]: 
        res = []
        r = (input.real**2 + input.imag**2)**(1/2)
        angle = phase(input)

        for k in range(pow):
            root = complex((r ** (1/pow)) * (cos((angle + 2 * pi * k) / pow) + 1j * sin((angle + 2 * pi * k) / pow)))
            real = round(root.real, self.precision)
            imag = round(root.imag, self.precision)

            if real == 0:
                res.append(f'{imag:+g}i')
            elif imag == 0:
                res.append(f'{real:g}')
            else:
                res.append(f"{real:g}{imag:+g}i")

        return res


    def _parse_exp(self) -> Any:
        # Да простит меня бог и многоуважаемые проверяющие, но sympy как я понял не отдает Zerodivisionerror.
        # Была б моя воля, просто ловил бы его. А так приходиться колхозить по-страшному.

        if all(sym in '0123456789.,+-*/^() iIjJ' for sym in self.input): # никаких буков
            exp = self.input.replace('i', 'I').replace('j', 'I').replace(',', '.')

            if re.search(r'\d\s+\d|\d\.\s+|\.\s+\d|\d\s+\.', exp): # перехватываем порбел между цифрами, чтобы parse_expr не приняла это за неявное умножение
                raise ValueError("Invalid spaces")

            if re.search(r'(^|[^\d])\.(?!\d)', exp): # не даем интермпретировать условно 2. как 2.0
                raise ValueError("InvalidExpression")

            if re.search(r'/\s*0+(?:\.0+)?(?=\s*(?:$|[+\-*/^)]))', exp): # явное деление на ноль
                raise ZeroDivisionError('Devision by zero') 

            try:
                res = parse_expr(exp, local_dict={'I': I}, transformations=transformations)
            except:
                raise ValueError('Invalid expression')

            if res.has(zoo):
                raise ZeroDivisionError('Division by zero')

            if res.has(nan):
                raise ValueError('Invalid expression')

            
            if res.is_real:
                return float(res)
            return complex(res)
        else:
            return None

