class Car:
    # constructor(__init__ hay yaha pe)
    def __init__(self,brand,model):
        # self.brand hoga topublic hay
        # self.brand=brand
        # #self.__brand then private hay
        self.__brand=brand
        self.__model=model

    def get_brand(self):
        return self.__brand  + " "   

        # method
    def showName(self):
        return  f"{self.__brand} {self.__model}"
   
    # making static method
    @staticmethod
    def describe():
        return "Cars are means of transport"
    

    # ham kuchh hide karna chahte and 
    # main goal is overwrite nahi kar paye
    @property

    def model(self):
        return self.__model

my_car=Car("Tata","safari")
print(my_car.showName())
# print(my_car.__brand)
print(my_car.get_brand())
print(Car.describe())
# my_car.model="abcc"
print(my_car.model,"model it is")





# # inheritance___________________________c
# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         # yeha super() se prent class matlab hay 
#         super().__init__(brand,model)
    
#         self.battery_size=battery_size

# my_tesla=ElectricCar("Tesla","model S","85KWh")        


# print(my_tesla.model)
# print(my_tesla.showName())

# encapsulation---------------------------------


# static methods:






