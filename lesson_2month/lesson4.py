class ElectoCar:
    def __init__(self,power,battery):
        self.power = power
        self.battery = battery

        def info(self):
            print(f"Мощность -{self.power}Vat /n   заряд баттерии - {self.battery}")

    def __repr__(self): # repr == print
            return (f"Мощность -{self.power}Vat /nз    аряд баттерии - {self.battery}")


car = ElectoCar(120,20000)
# car.info
print(car)
