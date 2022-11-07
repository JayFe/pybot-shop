'''
Created on 2 nov. 2022

@author: Jerrel
'''

from model.RobotType import RobotType
from model.SpyBot import SpyBot

class MyClass(object):
    
    robot_types = ["SpyBot"]
       
        
    def orderBot(self, robot_type):
        if (robot_type == RobotType.SPYBOT):
            return SpyBot()
        else:
            print("Unknown robot type")