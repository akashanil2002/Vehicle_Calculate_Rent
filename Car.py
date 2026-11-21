# Import the Vehicle parent class from Vehicle.py
from Vehicle import Vehicle

# Create a child class called Car
# It inherits attributes and methods from the Vehicle class
class Car(Vehicle):
     def calculate_rent(self): # Implement the abstract method from the parent class
          total_rent = (self.rental_price * self.vehicle_days) + 500 # Calculate basic rent by multiplying daily rental price by rental days
           # Add ₹500 to the total rent
          # Display the final car rental amount
          print('The total car rent price is - ', total_rent) 
          return total_rent # Return the calculated rental amount