# Import the Vehicle parent class from Vehicle.py
from Vehicle import Vehicle

# Create a child class called Bike
# It inherits attributes and methods from the Vehicle class
class Bike(Vehicle):
     def calculate_rent(self): # Implement the abstract method from the parent class
          total_rent = (self.rental_price * self.vehicle_days) + 100
          print('The total Bike rent price is - ', total_rent)
          return total_rent