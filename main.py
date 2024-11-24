import numpy as np
from RandomAgent import *
from game import ConnectX   
    



randomAgent = RandomAgent(name='AGENT-1')
randomAgent2 = RandomAgent(name='AGENT-2')
#todo
#humanAgent = Human()

#agentv1 = AgentV1()

game = ConnectX(players=[randomAgent,randomAgent2])



#x = game.test()
#print (x)
game.play()