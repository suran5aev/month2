"Принципы ООП"
"Наследование, Абстракция и Полиморфизм"



# class People: # Абстрактный класс и Родительский класс
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Parents(People): # Родительский класс
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def info(self):
#         print(f"имя - {self.name}, возраст - {self.age}")

#     def swim(self):
#         print("Я не умею плавать")

# mother = Parents("Нагима", 30)
# # print(mother.name, mother.age)
# mother.info()
# mother.swim()


# class Children(Parents): # Дочерний класс
#     def __init__(self, name, age, property):
#         super().__init__(name, age)
#         self.property = property
        
#     def swim(self):
#         print("Я умею плавать")

# child = Children("Alihan", 15, 0)
# child.info()
# child.swim()



class Animals:
    def __init__(self, name, eyes):
        self.name = name
        self.eyes = eyes

    def make_sound(self):
        pass

class Dogs(Animals):
    def make_sound(self):
        print("Gaf-Gaf")

class Cats(Animals):
    def make_sound(self):
        print("Meow")

class Fish(Animals):
    def make_sound(self):
        print("bul-bul")


dog = Dogs("Sharik", "Карие")
cat = Cats("Murka", "зеленые")
fish = Fish("Nemo", "Оранжевый")

dog.make_sound()
cat.make_sound()
fish.make_sound()