# #1
# class Fruits:
#     def __init__(self,name,color,weight):
#        self.name = name
#        self.color = color
#        self.weight = weight

#     def info(self):
#         print(f"Name - {self.name},color - {self.color}, weight - {self.weight}")
        
# apple = Fruits("Apple", "red", 20)
# apple.info()
# mango = Fruits("mango","yellow", 120)
# mango.info()




class Heroes:
    def __init__(self,name,role,health):
        self.name = name
        self.role = role
        self.health = health

    def info(self):
        print(f"Name - {self.name},  role - {self.role},   health - {self.health}")

    def do(self):
        print(f"{self.name} спасает город Ош")

tima = Heroes("Tima", "betmen", 99)
tima.info()
tima.do()
nurai = Heroes("nurai","supermen",98)
nurai.info()
nurai.do()
