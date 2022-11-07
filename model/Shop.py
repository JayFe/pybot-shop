'''
Created on 2 nov. 2022

@author: Jerrel
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, inventory):
        '''
        Constructor
    
        '''
        self.inventory = inventory
        
    def get_inventory(self):
         return self.inventory