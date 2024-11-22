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
    def set_token (self,token):
        pass