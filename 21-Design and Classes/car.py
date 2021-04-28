
from enum import Enum

class Direction(Enum):
    Left = "left"
    Right= "right"
    Up = "up"
    Down = "down"
    StandStill = "stand still"

class Car():
    """
    represents a car that has color, location (x ,y) and direction attributes. It also has go(), turn_left(), turn_right() functions
    """
    def __init__(self):
        self.color = "black"
        self.x = 0
        self.y = 0
        self.direction = Direction.StandStill.value
    
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.direction = Direction.StandStill.value

    def __str__(self):
        return "car color: {}\ncoordinates: ({},{})\ndirection: {}".format(self.color, self.x, self.y, self.direction)

    def go(self, unit):
        self.x = self.x + unit
        self.y = self.y + unit
    
    # def go(self, x, y):
    #     print("going")

    def turn_left(self):
        self.x = self.x - 1
        self.direction = Direction.Left.value
    
    def turn_right(self):
        self.x = self.x + 1
        self.direction = Direction.Right.value
    

car1 = Car("yellow", 0.0, 0.0)
car2 = Car("green", 1.0, 1.0)

car1.go(2)
car1.turn_left()
car1.go(1)
print(car1)

car2.turn_left()
car2.go(1)
car2.turn_right()
car2.go(2)
print(car2)