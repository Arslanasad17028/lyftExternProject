# from abc import ABC, abstractmethod

from Serviceable import Serviceable

class Car(Serviceable):
    def __init__(self,engine, battary):
        self.engine = engine
        self.battary = battary

    
    def needs_service(self):
        pass 
