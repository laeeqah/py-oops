 # Exercise 1
 # Exerise 2

class Bus:
    count= 0
# Creating two methods where yoU can change the color
# Keeping track of busses created
    def __init__(self, driver, seats, color):
        self.driver = driver
        self.seats = seats
        self.color = color
        self.update_count()

    def change_of_color (self, new_color):
        self.color = new_color

    def update_count(self):
        Bus.count = Bus.count + 1

bus1 = Bus("Tom", 66, "red")
bus2 = Bus("Tom", 66, input("new_color: "))

print(bus1.driver)
print(bus1.color)

print(bus2.color)
print(Bus.count)










