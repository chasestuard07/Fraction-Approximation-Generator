from Approximator import Approximator


if __name__ == "__main__":
    print("======================  Fraction Approximation Generator ======================")
    goalNum = float(input("Number to be approximated: "))
    print("--- Genetic Algorithm Values ---")
    numGens = int(input("   Number of generations: "))
    numMembers = int(input("    Population size: "))
    accuracyWeight = float(input("  Enter accuracy weight (0-1): "))
    sizeWeight = 1.0 - accuracyWeight

    a = Approximator(goalNum, numMembers, accuracyWeight, sizeWeight)
    
    a.initPopulation()
    for i in range(numGens):
        a.generateChildren()
        a.randomizePopulation()
        a.printWinner()
    input("Press Enter to exit...")