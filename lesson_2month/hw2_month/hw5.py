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
            return self.number_1 / self.number_2

        def __floordiv__(self, other):     
                return self.number_1 // other.number_2
num1 = MagicCalculator(10, 5)
num2 = MagicCalculator(3, 2)

print (num1 + num2)
print (num1 - num2)
print (num1 * num2)
print (num1 / num2)
print (num1 // num2)




#Доп дз 
class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def __lt__ (self,other):
        return self.year < other.year
    def __eg__(self,other):
        return self.year == other.year
    def __le__(self,other):
        return self.year <= other.year
    def __gt__(self,other):
        return self.year > other.year
    def __ne__(self,other):
        return self.year != other.year 
    def __str__(self):
        return f"{self.title},{self.author},{self.year}"
book1 = Book ("ЧУДО", 'Я' ,2024)
book2 = Book ('бизнес','Элиза',2022)
print(book1)
print(book2)
print(book1 < book2)
print(book1 == book2)
print(book1 <= book2)
print(book1 > book2)
print(book1 != book2)

