from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_name, vehicle_days, rental_price):
        self.vehicle_name = vehicle_name
        self.vehicle_days = vehicle_days
        self.__rental_price = rental_price

    @property
    def rental_price(self):
        return self.__rental_price

    def display_details(self):
         print('Vehicle name : ', self.vehicle_name)
         print('Vehicle rented days : ', self.vehicle_days)
         print('Rental price : ', self.rental_price)

    @abstractmethod

    def calculate_rent(days):
         pass