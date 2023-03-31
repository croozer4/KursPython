from abc import ABC, abstractmethod
import math

class Ksztalt(ABC):
    @abstractmethod
    def oblicz_pole(self):
        pass
    
    @abstractmethod
    def oblicz_obwod(self):
        pass

class Prostokat(Ksztalt):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def oblicz_pole(self):
        return self.a * self.b
    
    def oblicz_obwod(self):
        return 2 * (self.a + self.b)

class Kolo(Ksztalt):
    def __init__(self, r):
        self.r = r
    
    def oblicz_pole(self):
        return math.pi * self.r ** 2
    
    def oblicz_obwod(self):
        return 2 * math.pi * self.r

prostokat = Prostokat(5, 10)

print(prostokat.oblicz_pole())
print(prostokat.oblicz_obwod())

kolo = Kolo(3)

print(kolo.oblicz_pole())
print(kolo.oblicz_obwod())
