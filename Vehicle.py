# Import ABC and abstractmethod from the abc module
from abc import ABC, abstractmethod

# Create an abstract parent class called Vehicle
class Vehicle(ABC): # Constructor: Initialises vehicle details
    def __init__(self, vehicle_name, vehicle_days, rental_price): 
        self.vehicle_name = vehicle_name # Store the vehicle name
        self.vehicle_days = vehicle_days # Store the number of days the vehicle is rented
        self.__rental_price = rental_price # Store rental price as a private variable (Encapsulation)

# Property decorator provides controlled access to private rental price
    @property
    def rental_price(self):
        return self.__rental_price

# Method to display vehicle information
    def display_details(self):
         print('Vehicle name : ', self.vehicle_name)
         print('Vehicle rented days : ', self.vehicle_days)
         print('Rental price : ', self.rental_price) # Display the rental price using the property

# Abstract method: Child classes must implement this method
    @abstractmethod

    def calculate_rent(days):
         pass