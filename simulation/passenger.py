
class Passenger:
    def __init__(self, pickup_location, dropoff_location):
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location  
        self.data = []  

    def getPickupLocation(self):
        return self.pickup_location
    
    def getDropoffLocation(self):
        return self.dropoff_location

    def requestRide(self):
        print("request a ride")
        
# - attributes:
#   - pickup location, tuple
#   - dropoff location, tuple

# - methods (actions):
#   - request a ride
#   - if time permits, add walk fenctionality to simulate peoples' walking on the sidewalk