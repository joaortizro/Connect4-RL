import numpy as np
from abc import abstractmethod
import random



class Agent:
    def __init__(self,name):
        self.name=name
    
    @abstractmethod
    def do_action (self) -> int:
        pass
    
    @abstractmethod
    def set_grid (self,grid):
        pass
    
    @abstractmethod
    def set_token (self,token):
        pass
    
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

   
    
class ConnectX :
    def __init__(
            self,
            dimensions=(7,6),
            x = 4,
            players=[
              Random('AGENT-1'),
              Random('AGENT-2')   
            ],
            intial_player = 0,
            ):
        self.n= dimensions[0] # N rows of the grid
        self.m = dimensions[1] # M cols of the grid 
        self.grid = np.full((self.n, self.m),None)
        self.x = x # the amount of dots required to finish a game
        self.turn = 0 # the amount of turns 
        self.state = None
        self.players=players
        self.initial_player = intial_player
        self.current_player = players[intial_player] #by default initial player is RED
        self.current_player.set_token('R')#setea la ficha que va a usar
        self.players[1].set_token('A')
        
    def get_grid(self):
        return self.grid
    
    def set_grid(self,i,j,s):
        self.grid[i][j]=s
    
    def get_current_player(self):
        return self.current_player
    
    def get_current_state(self):
        return self.state
    
    def get_turn(self):
        return self.turn
    
    def terminal_state(self):
        return self.turn == (self.m * self.n)-1
    
    def next_player(self):
        index = self.turn%2
        self.current_player = self.players[index]
    
    def get_posible_actions (self):
        possible_actions = []
        for i in range(self.n):
            for j in range(self.m):
                if (self.grid[i][j]==None):
                    possible_actions.append((i,j))
        return possible_actions

    #def do_action(self):
        # should return a tuple (i,j) that represents the dot position
        #possible_actions = self.get_posible_actions()
        #choice = random.choice(possible_actions)
        
        #if self.get_current_player() == self.initial_player:
        #    self.set_grid(choice[0],choice[1],'R')
        #else:
        #    self.set_grid(choice[0],choice[1],'A')
        
    def play(self):
        while (True):
            print(self.turn)
            if(self.terminal_state()):
                break
            else :
                print(self.get_grid())
                self.current_player.set_grid(self.get_grid())
                action = self.current_player.do_action()
                self.set_grid(i=action[0],j=action[1],s=action[2])
                self.turn+=1
                self.next_player()



randomAgent = Random(name='AGENT-1')
randomAgent2 = Random(name='AGENT-2')
#todo
#humanAgent = Human()

#agentv1 = AgentV1()

game = ConnectX(players=[randomAgent,randomAgent2])



game.play()
