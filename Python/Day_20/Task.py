from abc import ABC,abstractmethod

class bike(ABC):
    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def gear(self):
        pass

    def lights(self):
        pass

class purchase(bike):
    def engine(self):
        print("Engine present")
    
    def gear(self):
        print("Gear present")
    
    def name(self):
        print("Honda")

    def wheels(self):
        print("Wheels")

purchase_1 = purchase()

purchase_1.name()
purchase_1.engine()
purchase_1.gear()
purchase_1.wheels()