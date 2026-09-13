from math import cos, sin, pi
from cmath import phase

class Calculator:

    status: str

    def __init__(self, input: str) -> None:
        self.input = input.strip()
        self._analyze_input()


    def calculate(self):
        if self.status == 'complex':
            return self._complex_square_root(self.input)
        elif self.status == 'positive':
            return self._basic_square_root(self.input)
        elif self.status == 'negative':
            return self._negative_root(self.input)


    def _basic_square_root(self, input: str) -> tuple[float]:
        number = float(input)

        return number ** (1/2), -(number**(1/2))


    def _negative_root(self, input: str) -> tuple[complex]:
        number = complex(input)

        return number ** (1/2), -(number ** (1/2))


    def _complex_square_root(self, input: str) -> list[complex]: # эта штука нужна во первых для того, чтобы можно было легко и непринужденно поменять степень корня
        res = []
        z = complex(input.replace(' ', '').replace('i', 'j'))
        r = (z.real**2 + z.imag**2)**(1/2)
        angle = phase(z)

        for k in range(2):
            root = (r ** (1/2)) * (cos((angle + 2 * pi * k) / 2) + 1j * sin((angle + 2 * pi * k) / 2))
            res.append(root)

        return res

    def _analyze_input(self) -> None:
        if 'i' in self.input or 'j' in self.input:
            self.status = 'complex'

        else:
            number = float(self.input)

            if number < 0:
                self.status = 'negative'
            else:
                self.status = 'positive'