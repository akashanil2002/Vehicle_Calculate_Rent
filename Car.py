from Vehicle import Vehicle

class Car(Vehicle):
     def calculate_rent(self):
          total_rent = (self.rental_price * self.vehicle_days) + 500
          print('The total car rent price is - ', total_rent)
          return total_rent