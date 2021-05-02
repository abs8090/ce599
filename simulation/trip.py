
class Trip:
    def __init__(self, id, status, startTime, endTime, passenger, driver):
        self.id = id
        self.status = status
        self.startTime = startTime
        self.endTime = endTime
        self.passenger = passenger
        self.driver = driver
    

# - attributes:
#     - id 
#     - trip status
#     - trip start time, starts when passenger is picked up
#     - trip end time, when passenger is dropped off
#     - trip pick up location, tuple 
#     - trip dropoff location, tuple
#     - Uber driver object, used to connect a driver with a passenger and to know how many trips a driver has completed. trips records will
#      be stored in an svc file and the columns will be the trip class attributes.

# - methods (actions):
