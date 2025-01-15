from abc import ABC, abstractmethod

class vehicle(ABC):

    def drive(self):
        print("Vehicle is in driving mode")

    @abstractmethod
    def start_engine(self):
        pass

class car(vehicle):
    def start_engine(self):
        print("Car engine is starting")
        