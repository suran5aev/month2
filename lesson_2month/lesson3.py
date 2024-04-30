"Инкапсуляция"

class Laptops:
    def __init__(self,model, os,displey):
        self.model = model      #Публичный
        self._os =os   #Защищенный
        self.displey = displey    #Приватный
    
    def info(self):
        print(f"model - {self.model},")
Acer = Laptops("Huawei","Windows 11", 512)
print(Acer.model)
print(Acer._os)
print(Acer.displey)