class Car:

    #! Class Variable
    total_car=0

    def __init__(self,brand,model):   #? __init__ => constructor
        # ^ self represent the instance of the class
        self.__brand=brand  
        self.__model=model
        Car.total_car+=1

    
    #? Encapsulation : Getter and Setter methods of attributes

    def get_brand(self):
        return self.__brand+"!"
    
    def get_model(self):
        return self.__model+"!"
    
    def set_model(self,model):
        self.__model=model

    def set_brand(self,brand):
        self.__brand=brand
   
    def full_name(self):
        return f"{self.__brand}:{self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"
    

    #? static method

    @staticmethod
    def general_description():
        return "Cars are means of transport"
    

    #? Property Decorator

    @property
    def model(self):
        return self.__model


#! Inheritence

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def fuel_type(self):
        return "Electric Charge"


# print("\n --- Class & Object----")

"""
my_car = Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())


my_new_car = Car("Tata","Safari")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.full_name())

"""

# print("\n --- Inheritence ----")

my_tesla = ElectricCar("Tesla","Model S","85kWh")


# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))


# print(my_tesla.model)
# print(my_tesla.__brand)


# print("\n --- Encapsulation ----")
# print(my_tesla.get_brand())
# print(my_tesla.full_name())

# my_tesla.set_model("Model X")
# print(my_tesla.get_model())
# print(my_tesla.full_name())


# print("\n-----Polymorphism-------")

# print(my_tesla.fuel_type())

safari = Car("Tata","Safari")
# print(safari.fuel_type())

# print("\n-----Class Variable-------")
safariThree = Car("Tata","Nexon")

# print(safari.total_car)

# print(Car.total_car)

"""

print("\n-----Static Method-------")

# print(safariThree.general_description())
print(Car.general_description())

"""


"""
print("\n-----Property Decorator-------")

# safari.model="City"

# print(safari.model)


print(safari.model)
"""

# print("\n----- Class Inheritance and isinstance() Function-------")


# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))


# * Multiple Inheritence


class Battery:
    def battery_info(self):
        return "This is battery"
    
    def hello(self):
        return "hello1"


class Engine:
    def engine_info(self):
        return "This is engine"
    
    def hello(self):
        return "hello2"


class ElectricCarTwo(Battery,Engine,Car):
    pass


my_new_tesla = ElectricCarTwo("Tesla","Model S")

print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())

print(my_new_tesla.hello())