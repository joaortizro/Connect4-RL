from abc import abstractmethod

class Agent:
    """
    This is an abstract definition of an agent
    """
    def __init__(self,name):
        self.name=name
    
    @abstractmethod
    def do_action (self) -> int:
        pass
    
    @abstractmethod
    def set_grid (self,grid):
        pass
    
    @abstractmethod
    def set_grid_pos (self,grid):
        pass
    
    @abstractmethod
    def set_piece (self,token):
        pass
    
    @abstractmethod
    def get_piece(self):
        pass