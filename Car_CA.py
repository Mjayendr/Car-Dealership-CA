# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 13:29:50 2017
@author: Jay Monpara
Student ID = 10360474
"""


# Create Car Classs
class Car(object):
    # implement the car object
    # define attributes
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        self.enginesize = ''

# creating Methods       
    def getColour(self):
        return self.__colour

    def getMake(self):
        return self.__make

    def getMileage(self):
        return self.__mileage
    
    def setColour(self, colour):
        self.__colour = colour

    def setMake(self, make):
        self.__make = make 

    def setMileage(self, mileage):
        self.__mileage = mileage

    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage

# create subclasses
        
class ElectricCar(Car):

# create object of electric car
    def __init__(self):
        Car.__init__(self)
        self.__FuelCells = 0

# Methods for electic car
    def getFuelCells(self):
        return self.__FuelCells

    def setFuelCells(self, value):
        self.__FuelCells = value

class PetrolCar(Car):
# create object for petrol car
    def __init__(self):
        Car.__init__(self)
        self.__Cylinders = 0
# methods for petrol car
    def getCylinders(self):
        return self.__Cylinders

    def setCylinders(self, value):
        self.__Cylinders = value

class HybridCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__FuelType = ''

    def getFuelType(self):
        return self.__FuelType

    def setFuelType(self, Fuel):
        self.__FuelType = Fuel
    
class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__Transmission = ''

    def getTransmission(self):
        return self.__Transmission

    def setTransmission(self, type):
        self.__Transmission = type
               
# create car inventory
class Car_Fleet(object):
    def __init__(self):
        self.__cars = []
        self.__numAvailable = 40
        self.petrol_cars = 20
        self.electric_cars = 4
        self.diesel_cars = 8
        self.hybrid_cars = 8
        
# create dealership
class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []
# get data from inventory for type of cars owned by a delear.
        self.total_cars = Car_Fleet()
        self.owned_petrol_cars = self.total_cars.petrol_cars
        self.owned_electric_cars = self.total_cars.electric_cars
        self.owned_diesel_cars = self.total_cars.diesel_cars
        self.owned_hybrid_cars = self.total_cars.hybrid_cars

# Creating objects for each car type     
    def create_stock(self):
        for i in range(self.owned_electric_cars):
           self.electric_cars.append(ElectricCar())
        for i in range(self.owned_petrol_cars):
           self.petrol_cars.append(PetrolCar())
        for i in range(self.owned_diesel_cars):
           self.diesel_cars.append(DieselCar())
        for i in range(self.owned_hybrid_cars):
           self.hybrid_cars.append(HybridCar())
        
        print 'petrol cars in stock ' + str(len(self.petrol_cars))
        print 'electric cars in stock ' + str(len(self.electric_cars))
        print 'diesel cars in stock ' + str(len(self.diesel_cars))
        print 'hybrid cars in stock ' + str(len(self.hybrid_cars))
        
# printing current stock   
    def stock_count(self):
        print 'petrol cars in stock ' + str(len(self.petrol_cars))
        print 'electric cars in stock ' + str(len(self.electric_cars))
        print 'diesel cars in stock ' + str(len(self.diesel_cars))
        print 'hybrid cars in stock ' + str(len(self.hybrid_cars))

# setting get function to use in unit testing  
    def get_electric_cars_stock(self):
        self.available_electric_cars = len(self.electric_cars)
        return self.available_electric_cars
    def get_petrol_cars_stock(self):
        self.available_petrol_cars = len(self.petrol_cars)
        return self.available_petrol_cars
    def get_diesel_cars_stock(self):
        self.available_diesel_cars = len(self.diesel_cars)
        return self.available_diesel_cars
    def get_hybrid_cars_stock(self):
        self.available_hybrid_cars = len(self.hybrid_cars)
        return self.available_hybrid_cars
    
        
# creating return for electric car
    def return_electric_car(self,amount):
        total = 0
        expected_total = amount + len(self.electric_cars)     # calculating total number of cars if accepting return
        if expected_total <= self.owned_electric_cars:  # validating expected total with stock of electric cars
            while total <amount:
                self.electric_cars.append(ElectricCar())  # adding car to available car list
                total = total + 1
            print '\nThank you, you have successfully returned ' + str(amount) + ' electric cars. ' 
        else:
            print '\nSorry, number of returned cars are more than expected!'
# rent electric car           
    def rent_electric_car(self, amount):
        if len(self.electric_cars) < amount:
            print 'Sorry, Nothing to rent, Please try again later'
        else:    
            rented_electric_cars = 0
            while rented_electric_cars < amount:
               self.electric_cars.pop()       # poping cars from the available car list
               rented_electric_cars = rented_electric_cars + 1
            print '\nThank you, you have successfully rented ' + str(amount) + ' electric cars. ' 
# return pertrol car          
    def return_petrol_car(self, amount):
        total = 0
        expected_total = amount + len(self.petrol_cars)
        if expected_total <= self.owned_petrol_cars:
            while total <amount:
                self.petrol_cars.append(PetrolCar())
                total = total + 1
            print '\nThank you, you have successfully returned ' + str(amount) + ' petrol cars. '
        else:
            print '\nSorry, number of returned cars are more than expected!'
            
# rent petrol car           
    def rent_petrol_car(self, amount):
        if len(self.petrol_cars) < amount:
            print 'Sorry, Nothing to rent, Please try again later'
        else:
            rented_petrol_cars = 0
            while rented_petrol_cars < amount:
               self.petrol_cars.pop()
               rented_petrol_cars = rented_petrol_cars + 1
            print '\nThank you, you have successfully rented ' + str(amount) + ' petrol cars. '

# return diesel cars           
    def return_diesel_car(self, amount):
        total = 0
        expected_total = amount + len(self.diesel_cars)
        if expected_total <= self.owned_diesel_cars:
            while total <amount:
                self.diesel_cars.append(DieselCar())
                total = total + 1
            print '\nThank you, you have successfully returned ' + str(amount) + ' diesel cars. '
        else:
            print '\nSorry, number of returned cars are more than expected!'

# rent diesel car              
    def rent_diesel_car(self, amount):
        if len(self.diesel_cars) < amount:
            print 'Sorry, Nothing to rent, Please try again later'    
        else:
            rented_diesel_cars = 0
            while rented_diesel_cars < amount:
               self.diesel_cars.pop()
               rented_diesel_cars = rented_diesel_cars + 1
            print '\nThank you, you have successfully rented ' + str(amount) + ' diesel cars. '

# return hybrid cars           
    def return_hybrid_car(self,amount):
        total = 0
        expected_total = amount + len(self.hybrid_cars)
        if expected_total <= self.owned_hybrid_cars:
            while total <amount:
                self.hybrid_cars.append(HybridCar())
                total = total + 1
            print '\nThank you, you have successfully returned ' + str(amount) + ' hybrid cars. '
        else:
            print '\nSorry, number of returned cars are more than expected!'
# rent hybrid cars
    def rent_hybrid_car(self, amount):
        if len(self.hybrid_cars) < amount:
            print 'Sorry, Nothing to rent, Please try again later'
        else:
            rented_hybrid_cars = 0 
            while rented_hybrid_cars < amount:
               self.hybrid_cars.pop()
               rented_hybrid_cars = rented_hybrid_cars + 1
            print '\nThank you, you have successfully rented ' + str(amount) + ' hybrid cars. '

# informing user for available options       
    def process_options(self):
        ask = raw_input('would you like to rent a car or return a car ? \n enter 1 for rent \n enter 2 for return \n enter 3 to check available stock or \n enter 0 to exit the program ')
        if ask == '1':
            self.process_rental()
            self.process_options()  #  invoking function to return to available options

        elif ask == '2':
            self.process_return()
            self.process_options()  #  invoking function to return to available options

        elif ask == '3':
            self.stock_count()
            self.process_options()  #  invoking function to return to available options

        elif ask == '0':
            print 'Bye Bye '
        else:
            print '\nSorry invalid input, please try again '
        
 
# Creating rental process       
    def process_rental(self):
        answer = raw_input('\nwhat type of car would you like to rent? p/d/h/e - ')
        amount = int(raw_input('\nhow many cars would you like to rent? '))
        if answer == 'p':
            self.rent_petrol_car(amount)
        elif answer == 'd':
            self.rent_diesel_car(amount)
        elif answer == 'h':
            self.rent_hybrid_car(amount)
        elif answer == 'e':
            self.rent_electric_car(amount)
        else:
            print '\nSorry invalid entry, please try again'
            self.process_rental() # invoking rental function in case of invalid input
            
# creating return process
    def process_return(self):
        car_return = raw_input('which car you want to return, p/d/h/e? = ')
        amount = int(raw_input('\nHow many cars you want to retrun? = '))
            
        if car_return == 'p':
            self.return_petrol_car(amount)
        elif car_return == 'd':
            self.return_diesel_car(amount)
        elif car_return == 'h':
            self.return_hybrid_car(amount)
        elif car_return == 'e':
            self.return_electric_car(amount)
        else:
            print '\nSorry invalid entry, please try again'
            self.process_return() # # invoking return function in case of invalid input
        
            
        