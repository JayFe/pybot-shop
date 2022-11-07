'''
Created on 7 nov. 2022

@author: Jerrel
'''
from model.Robot import Robot
from model.PowerSupply import PowerSupply
import uuid


class SpyBot(Robot):
    price = 2400;
    powerSupply = PowerSupply.DARK_MATTER


    def __init__(self):
        uuid = uuid.uuid4()
    
    def get_power_supply(self):
        return self.powerSupply;
    
    def get_price(self):
        return self.price
      
    def get_type(self):
        return self.__class__
        