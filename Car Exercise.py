class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


    def __str__(self):
        return f'The {self.color} car hae {self.mileage:,} miles.'
