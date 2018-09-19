# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:38:39 2017
@author: Jay Monpara, 
student ID = 10360474

"""
import unittest

from Car_CA import Car, ElectricCar, PetrolCar, HybridCar, DieselCar, Dealership

# test the car functionality
class TestCar(unittest.TestCase):

# Creating objects in the memory.
    def setUp(self):
        self.car = Car()
        self.electriccar = ElectricCar()
        self.petrolcar = PetrolCar()
        self.hybridcar = HybridCar()
        self.dieselcar = DieselCar()
        self.dealership = Dealership()
        self.dealership.create_stock()
        

# Testing for car make, colour and mileage changes.
        
    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())

    def test_car_make(self):
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())

    def test_car_colour(self):
        self.assertEqual('', self.car.getColour())
        self.car.setColour('red')
        self.assertEqual('red', self.car.getColour())

# Testing for Electric Car fuel cell numbers.     
    def test_electric_car_fuelcells(self):
        self.assertEqual(0, self.electriccar.getFuelCells())
        self.electriccar.setFuelCells(4)
        self.assertEqual(4,self.electriccar.getFuelCells())

# Testing for petrol cay cylinder counts       
    def test_petrol_car_cylinders(self):
        self.assertEqual(0,self.petrolcar.getCylinders())
        self.petrolcar.setCylinders(6)
        self.assertEqual(6,self.petrolcar.getCylinders())

# Testing for hybrid car fuel type.        
    def test_hybrid_car_fueltype(self):
        self.assertEqual('',self.hybridcar.getFuelType())
        self.hybridcar.setFuelType('Petrol')
        self.assertEqual('Petrol', self.hybridcar.getFuelType())

# Testing for diesel car transmission type.       
    def test_diesel_car_transmission(self):
        self.assertEqual('', self.dieselcar.getTransmission())
        self.dieselcar.setTransmission('Automatic')
        self.assertEqual('Automatic', self.dieselcar.getTransmission())

# Testing electric car rental function        
    def test_electic_cars_rental(self):
        self.dealership.rent_electric_car(2)
        self.assertEqual(2, self.dealership.get_electric_cars_stock())

# Testing electric car return function    
    def test_electric_cars_return(self):
        self.dealership.return_electric_car(2)
        self.assertEqual(4, self.dealership.get_electric_cars_stock())

# Testing petrol car rental function        
    def test_petrol_cars_rental(self):
        self.dealership.rent_petrol_car(5)
        self.assertEqual(15, self.dealership.get_petrol_cars_stock())

# Testing petrol car return function         
    def test_petrol_cars_return(self):
        self.dealership.return_petrol_car(5)
        self.assertEqual(20, self.dealership.get_petrol_cars_stock())

# Testing diesel car rental function
    def test_diesel_cars_rental(self):
        self.dealership.rent_diesel_car(2)
        self.assertEqual(6, self.dealership.get_diesel_cars_stock())

# Testing diesel car return function         
    def test_diesel_cars_return(self):
        self.dealership.return_diesel_car(2)
        self.assertEqual(8, self.dealership.get_diesel_cars_stock())
        
# Testing hybrid car rental function
    def test_hybrid_cars_rental(self):
        self.dealership.rent_hybrid_car(3)
        self.assertEqual(5, self.dealership.get_hybrid_cars_stock())

# Testing hybrid car return function         
    def test_hybrid_cars_return(self):
        self.dealership.return_hybrid_car(3)
        self.assertEqual(8, self.dealership.get_hybrid_cars_stock())
        

if __name__ == '__main__':
    unittest.main()
