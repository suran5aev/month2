class MagicCalculator:
        def __init__(self, number_1, number_2):
            self.number_1 = number_1
            self.number_2 = number_2

        def __add__(self, other):
            return self.number_1 + other.number_2

        def __sub__(self, other):
            return self.number_1 - other.number_2

        def __mul__(self, other):
            return self.number_1 * other.number_2

        def __truediv__(self, other):
            if other.number_2 != 0:
                return self.number_1 / other.number_2
            else:
                return "Деление на ноль не допускается"

        def __floordiv__(self, other):
            if other.number_2 != 0:
                return self.number_1 // other.number_2
            else:
                return "Деление на ноль не допускается"
            
num1 = MagicCalculator(10, 5)
num2 = MagicCalculator(3, 2)

print (num1 + num2)
print (num1 - num2)
print (num1 * num2)
print (num1 / num2)
print (num1 // num2)
