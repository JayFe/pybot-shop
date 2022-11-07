'''
Created on 7 nov. 2022

@author: Jerrel
'''
from abc import ABC, abstractmethod

class Robot(ABC):
    
    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_price(self):
        pass
    
    @abstractmethod
    def get_power_supply(self):
        pass