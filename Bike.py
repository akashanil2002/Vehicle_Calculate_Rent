from Vehicle import Vehicle

class Bike(Vehicle):
     def calculate_rent(self):
          total_rent = (self.rental_price * self.vehicle_days) + 100
          print('The total Bike rent price is - ', total_rent)
          return total_rent