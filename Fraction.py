import math
import random

class Fraction:
    def __init__(self, numerator, denominator, goal):
        self.n = numerator
        self.d = denominator
        self.goal = goal

    def value(self):
        return self.n / self.d
    
    def fitness(self, accWeight, sizeWeight):
        if(self.d%10 == 0):
            return 100
        if(math.gcd(self.n, self.d) != 1):
            return 100
        if(self.value() <= 0):
            return 100
        

        return accWeight * 100 * abs((self.goal - self.value())) + sizeWeight * (math.log10(self.n) + math.log10(self.d))

    
    def randomize(self):
        self.n += random.randint(-10, 10)
        self.d += random.randint(-10, 10)
        if(self.d <= 0):
            self.d = 1
        if(self.n < 0):
            self.n = 0