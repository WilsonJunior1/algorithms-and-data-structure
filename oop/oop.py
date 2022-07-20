class Car():
    def __init__(self, color, year):
        self.color = color
        self.year = year

    def accelerate(self):
        print("Accelerating...")

    def breakCar(self):
        print("Breaking...")

    def stop(self):
        print("Stoping...")

civic = Car('white', 2021)

civic.accelerate()
civic.breakCar()
civic.stop()
print(civic.color)
print(civic.year)
