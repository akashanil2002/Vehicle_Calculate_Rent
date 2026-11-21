# Import the parent Vehicle class
from Vehicle import Vehicle
# Import the Car child class
from Car import Car
# Import the Bike child class
from Bike import Bike

# Create an object of the Car class
Car = Car('Alto', 5 , 400) 
Car.display_details() # Display the car's details
Car.calculate_rent() # Calculate and display the total car rental price

# Create an object of the Bike class
Bike = Bike('R15', 6 , 100)
Bike.display_details()  # Display the bike's details
Bike.calculate_rent()  # Calculate and display the total bike rental price


#Output
# Vehicle name :  Alto
# Vehicle rented days :  5
# Rental price :  400
# The total car rent price is -  2500
# Vehicle name :  R15
# Vehicle rented days :  6
# Rental price :  100
# The total Bike rent price is -  700