from Agent import *
import random

class Random(Agent):
    def __init__(self,name):
        super().__init__(name)
    
    def set_grid(self,grid):
        self.grid=grid
        
    def set_token(self,token):
        self.token=token
    
    def get_posible_actions (self):
        possible_actions = []
        for i in range(self.n):
            for j in range(self.m):
                if (self.grid[i][j]==None):
                    possible_actions.append((i,j))
        return possible_actions
    
    def do_action(self):
        possible_actions = self.get_posible_actions()
        choice = random.choice(possible_actions)
        return (choice[0],choice[1],self.token)
    
    def get_posible_actions (self):
        possible_actions = []
        for i in range(7):
            for j in range(6):
                if (self.grid[i][j]==None):
                    possible_actions.append((i,j))
        return possible_actions