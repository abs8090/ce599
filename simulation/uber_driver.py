
class UberDriver:
    def __init__(self, id, current_location, status):
        self.id = id
        self.current_location = current_location
        self.status = status # with a passenger or not. used to assign a driver with a trip
        self.data = []

    def getCurrentLocation(self):
        return self.current_location
    
    def receiveTripRequest():
        print("recieve trip request")
    
    def acceptTripRequest(self):
        print("accept trip request")
    
    def goPickupPassenger(self, passenger):
        print("on the map, direct this driver object towards passenger location")
        print("the passenger argument is a Passenger object and used to get passenger pickup and dropoff locations")
    
    def pickupPassenger(self, trip):
        print("change uber driver status")

    def startTrip(self, passenger, trip):
        print("use the passenger object to get dropoff location.")
        print("change trip status to active")

    def endTrip(self, passenger, trip):
        print("use the passenger object to get dropoff location.")
        print("change trip status to complete to save trip data")
        
# - attributes:
#     - id 
#     - current_location, tuple
#     - 

# - methods (actions):
#     - receive trip request
#     - accept trip request
#     - go pickup passenger
#     - pickup passenger
#     - start trip, goes to passenger's desired dropoff location
#     - end/complete trip
