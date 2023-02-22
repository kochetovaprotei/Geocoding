class Car:

    def __init__(self, type_car, year, capacity, price, mileage):
        self.type = type_car
        self.year = year
        self.capacity = capacity
        self.price = price
        self.mileage = mileage
        self.number_of_wheels = 4

    def description_car(self):
        """Описание машины"""
        description = "model - " + self.type + ", " + str(self.year) + ", capacity - " + str(self.capacity) + \
                      " l, price - " + str(self.price) + ' r, mileage - ' + str(self.mileage) + \
                      ' km, number_of_wheels - ' + str(self.number_of_wheels)
        print("Description: " + description)


class Truck(Car):

    def __init__(self, type_car, year, capacity, price, mileage):

        super().__init__(type_car, year, capacity, price, mileage)
        self.number_of_wheels = 8

    def description_car(self):
        """Описание машины"""
        description = "model - " + self.type + ", " + str(self.year) + ", capacity - " + str(self.capacity) + \
                      " l, price - " + str(self.price) + ' r, mileage - ' + str(self.mileage) + \
                      ' km, number_of_wheels - ' + str(self.number_of_wheels)
        print("Description for truck: " + description)


first_car = Car('Honda_Rafaga', 1997, 2, 1_000_000, 100_000)
first_car.description_car()

second_car = Truck('Ural', 1995, 15, 3_000_000, 200_000)
second_car.description_car()
