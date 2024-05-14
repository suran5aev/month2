import sys
class Game:
    def compare_numbers(self, num1, num2):
        if num1 > num2:
            return "Победитель игрок 1!"
        elif num1 < num2:
            return "Победитель игрок 2!"
        else:
            return "Они равны!"

game = Game()
numbers1 = int(input("Введите число игрок 1: "))
numbers2 = int(input("Введите число игрок 2: "))

result = game.compare_numbers(numbers1, numbers2)
print(result)