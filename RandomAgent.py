from Agent import *
import random

class RandomAgent(Agent):
    def __init__(self,name):
        super().__init__(name)
    
    def set_grid(self,grid):
        self.grid=grid
        dimensions = self.grid.shape
        self.n,self.m = dimensions
    
    def get_grid_pos(self,i,j):
        return self.grid[i][j]
    
    def set_piece(self,token):
        self.token=token
        
    def get_piece(self):
        return self.token
    
    def get_posible_actions (self):
        possible_actions = []
        for j in range (self.m):
            if (self.get_grid_pos(0,j)==None):
                possible_actions.append(j)
        print(possible_actions)
        return possible_actions
    
    def do_action(self):
        possible_actions = self.get_posible_actions()
        choice = random.choice(possible_actions)
        return choice