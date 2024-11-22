import numpy as np
from RandomAgent import *
   
    
class ConnectX :
    def __init__(
            self,
            n=6,
            m=7, 
            x = 4,
            players=[],
            intial_player = 0,
        ):
        self.n= n # N rows of the grid
        self.m = m # M cols of the grid 
        self.grid = np.full((self.n, self.m),None)
        self.x = x # the amount of connected dots required to finish a game
        self.turn = 0 # the amount of turns 
        self.state = None
        self.players=players
        self.initial_player = intial_player
        self.current_player = players[intial_player] #by default initial player is RED
        self.current_player.set_piece('R')#setea la ficha que va a usar
        self.players[1].set_piece('A')
        
    def get_grid(self):
        return self.grid

    def get_grid_pos(self,i,j):
        return self.grid[i][j]
    
    def set_grid_pos(self,i,j,s):
        self.grid[i][j]=s
    
    def get_current_player(self):
        return self.current_player
    
    def get_current_state(self):
        return self.state
    
    def get_turn(self):
        return self.turn
    
    def terminal_state(self):
        return self.turn == (self.m * self.n)
    
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
    
    def drop_piece (self,column):
        for i in range (self.n-1,-1,-1):
            if (self.get_grid_pos(i,column)==None):
                self.set_grid_pos(i,column,self.current_player.get_piece())
                break
    
    def play(self):
        while (True):
            print(self.turn)
            print(self.get_grid())
            if(self.terminal_state()):
                break
            else :
                self.current_player.set_grid(self.get_grid())
                action = self.current_player.do_action()
                self.drop_piece(action)
                self.turn+=1
                self.next_player()
    
    def test(self):
        print(self.get_grid())
        self.current_player.set_grid(self.get_grid())
        self.drop_piece(0)
        print(self.get_grid())
        self.turn+=1
        self.next_player()

randomAgent = RandomAgent(name='AGENT-1')
randomAgent2 = RandomAgent(name='AGENT-2')
#todo
#humanAgent = Human()

#agentv1 = AgentV1()

game = ConnectX(players=[randomAgent,randomAgent2])



game.play()
