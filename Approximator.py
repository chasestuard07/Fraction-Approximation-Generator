from Fraction import Fraction

import math
import random 

class Approximator:
    def __init__(self, goalNum, numMembers, accWeight, sizeWeight):
        self.fractions = []
        self.goalNum = goalNum
        self.numMembers = numMembers
        self.accWeight = accWeight
        self.sizeWeight = sizeWeight

    #Initialize the population, giving pseudo-random values
    def initPopulation(self):
        for i in range(self.numMembers):
            self.fractions.append(Fraction(i + random.randint(0, 5), i+1 + random.randint(0, 5), self.goalNum))

    #Sort through the population based on fitness and return the top 10%
    def sortPopulation(self):
        self.fractions.sort(key=lambda f: f.fitness(self.accWeight, self.sizeWeight), reverse=False)
        if (len(self.fractions) < 10):
            return self.fractions[:1]
        else:
            return self.fractions[:int(self.numMembers*0.1)]
    
    #Given the remaining population, generate children to reach the initial population size
    def generateChildren(self):
        top_1 = self.sortPopulation()
        self.fractions = top_1
        for i in range(self.numMembers - len(top_1)):
            parent1 = top_1[random.randint(0,len(top_1) - 1)]
            parent2 = top_1[random.randint(0,len(top_1) - 1)]
            self.fractions.append(Fraction(parent1.n, parent2.d, self.goalNum))
    
    #Mutate the population (encourages new solutions)
    def randomizePopulation(self):
        for i in range(self.numMembers - 1):
            self.fractions[i+1].randomize()

    #Print the member with the best fitness value
    def printWinner(self):
        self.fractions.sort(key=lambda f: f.fitness(self.accWeight, self.sizeWeight), reverse=False)
        winner = self.fractions[0]
        print("Winner: ", winner.n, "/", winner.d, " = ", winner.n/winner.d)