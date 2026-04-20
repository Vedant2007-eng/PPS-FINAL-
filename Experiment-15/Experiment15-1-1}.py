# Base class
class Car:
    def __init__(self, brand, price, model, color):
        self.brand = brand
        self.price = price
        self.model = model
        self.color = color

    def display_details(self):
        print(self.brand)
        print(self.price)
        print(self.model)
        print(self.color)


# Derived class Car1
class Car1(Car):
    def display_details(self):
        print(self.brand)
        print(self.price)
        print(self.model)
        print(self.color)


# Derived class Car2
class Car2(Car):
    def display_details(self):
        print(self.brand)
        print(self.price)
        print(self.model)
        print(self.color)


# Input for Car1
data1 = input().split()
brand1 = data1[0]
price1 = float(data1[1])
model1 = data1[2]
color1 = data1[3]

# Input for Car2
data2 = input().split()
brand2 = data2[0]
price2 = float(data2[1])
model2 = data2[2]
color2 = data2[3]

# Create objects
car1 = Car1(brand1, price1, model1, color1)
car2 = Car2(brand2, price2, model2, color2)

# Display details
car1.display_details()
car2.display_details()

# # Read input
# car1_data = input().split()
# brand1, price1, model1, color1 = car1_data[0], float(car1_data[1]), car1_data[2], car1_data[3]

# car2_data = input().split()
# brand2, price2, model2, color2 = car2_data[0], float(car2_data[1]), car2_data[2], car2_data[3]

# # Create objects
# car1 = Car1(brand1, price1, model1, color1)
# car2 = Car2(brand2, price2, model2, color2)

# # Display details
# car1.display_details()
# car2.display_details()
