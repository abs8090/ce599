
class Sensor:

    def __init__(self, id, timeInterval):
        self.id = id
        self.data = []
        self.timeInterval = timeInterval

    def getId(self):
        return self.id
    
    def generateMessage(self, timeInterval): # time interval can thought of as number of messages/data a sensor generates during the simulation
        self.data.append = "data"
    
    def sendData(self, driver):
        driver.data = self.data
    