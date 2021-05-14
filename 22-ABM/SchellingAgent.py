"""
gde 4.2.2018
Adapted from Project Mesa Schelling Model example: 
https://github.com/projectmesa/mesa-schelling-example/blob/master/analysis.ipynb
but changed to run stand-alone. 
""" 

import random

class SchellingAgent():
    '''
    Schelling segregation agent
    '''
    def __init__(self, pos, grid, agent_type):
        '''
         Create a new Schelling agent.

         Args:
            pos: (x, y) Agent initial location.
            grid: a grid of the city, where 0=empty, 1=minority, 2=majority 
            agent_type: Indicator for the agent's type (minority=1, majority=2)
        '''
        self.pos = pos
        self.grid = grid
        self.type = agent_type
        self.x = pos[0]
        self.y = pos[1]
        self.grid[self.x][self.y] = self.type
        self.isHappy = False
        self.neighbors = 0
        self.sameType = 0
    
    def calculate_similarity(self):
        '''
        Calculates the similarity ratio for the agent.  Defined as:
            similarity = neighbors of same type / total (non-empty) neighbors
        '''
        print('Implement calculate_similarity()')

    def get_neighbors_total(self):
        isCorner = False
        self.neighbors = 0

        # if self.pos[0] == 0 or self.pos[0] == len(self.grid[0]) - 1:
        #     print("this is either on top line or bottom line")
        # else:
        #     print("not an edge cell")
        
        if self.pos[0] > 0:
            print("we can check pos above ")
            self.neighbors = self.neighbors + 1
        
        if self.pos[0] < len(self.grid[0]) - 1:
            print("we can check pos below")
            self.neighbors = self.neighbors + 1
        
        if self.pos[1] > 0:
            print("we can check pos on the left")
            self.neighbors = self.neighbors + 1
        
        if self.pos[1] < len(self.grid[1]) - 1:
            print("we can check pos on the right")
            self.neighbors = self.neighbors + 1

        if self.pos[0] > 0 and self.pos[1] > 0:
            print("we can check pos upper left")
            self.neighbors = self.neighbors + 1
        
        if self.pos[0] < len(self.grid[0]) - 1 and self.pos[1] > 0:
            print("we can check pos lower left")
            self.neighbors = self.neighbors + 1
        
        if self.pos[1] < len(self.grid[1]) - 1 and self.pos[0] > 0:
            print("we can check pos upper right")
            self.neighbors = self.neighbors + 1
        
        if self.pos[0] < len(self.grid[0]) - 1 and self.pos[1] < len(self.grid[1]) - 1:
            print("we can check lower right")
            self.neighbors = self.neighbors + 1
        
        return self.neighbors


    def is_happy(self): 
        '''
        The agent is happy if at least 30% of its neighbors are of the same type. 
        '''
        self.sameType = 0
        if self.pos[0] > 0:
            print("we can check pos above ")
            if self.grid[self.x - 1][self.y] == self.type:
                self.sameType = self.sameType + 1
        
        if self.pos[0] < len(self.grid[0]) - 1:
            print("we can check pos below")
            if self.grid[self.x + 1][self.y] == self.type:
                self.sameType = self.sameType + 1
        
        if self.pos[1] > 0:
            print("we can check pos on the left")
            if self.grid[self.x][self.y - 1] == self.type:
                self.type = self.type + 1
        
        if self.pos[1] < len(self.grid[1]) - 1:
            print("we can check pos on the right")
            if self.grid[self.x][self.y + 1] == self.type:
                self.type = self.type + 1

        if self.pos[0] > 0 and self.pos[1] > 0:
            print("we can check pos upper left")
            if self.grid[self.x - 1][self.y - 1] == self.type:
                self.sameType = self.sameType + 1
        
        if self.pos[0] < len(self.grid[0]) - 1 and self.pos[1] > 0:
            print("we can check pos lower left")
            if self.grid[self.x + 1][self.y - 1] == self.sameType:
                self.sameType = self.sameType + 1
        
        if self.pos[1] < len(self.grid[1]) - 1 and self.pos[0] > 0:
            print("we can check pos upper right")
            if self.grid[self.x - 1][self.y + 1] == self.sameType:
                self.sameType = self.sameType + 1
        
        if self.pos[0] < len(self.grid[0]) - 1 and self.pos[1] < len(self.grid[1]) - 1:
            print("we can check lower right")
            if self.grid[self.x + 1][self.y + 1] == self.sameType:
                self.sameType = self.sameType + 1

        if (self.sameType / self.neighbors) * 100.0 >= 30.0:
            print("happy")
            print( (self.sameType / self.neighbors) * 100.0)
        else:
            print("not happy")

    def move(self):
        '''
        Moves the agent to a randomly selected empty square.  
        '''
        print('Implement move')
        