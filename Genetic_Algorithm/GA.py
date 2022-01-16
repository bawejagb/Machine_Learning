import random as rd

def function1(x,y):
    return 2*x**3 - 5*y**2 - 30

def fitness(x,y):
    ans = function1(x,y)
    return abs(ans)

def  generatePop(pop_size):
    population = []
    for x in range(pop_size):
        population.append((rd.uniform(0,100), rd.uniform(0,100)))
    return population

def crossOver(p1, p2):
    c1 = (p1[0], p2[1])
    c2 = (p2[0], p1[1])
    f1 = fitness(c1[0], c1[1])
    f2 = fitness(c2[0], c2[1])
    if(abs(f1) < abs(f2)):
        return c1
    return c2

def mutate(newGen, percent):
    solution = []
    for crom in newGen:
        solution.append((crom[0]*rd.uniform((100-percent)/100, (100+percent)/100),
                        crom[1]*rd.uniform((100-percent)/100, (100+percent)/100)))
    return solution

def geneticAlgo(population, total_gen, percent):
    solution = []
    for crom in population:
        solution.append((fitness(crom[0], crom[1]), crom))
    solution.sort()
    bestSolution = solution[0]
    for x in range(total_gen):
        newGen = []
        p1 = solution[0]
        for p2 in solution[1:]:
            newGen.append(crossOver(p1[1],p2[1]))
        newGen.append(crossOver(solution[1][1],solution[2][1]))
        newGen  = mutate(newGen, percent)
        solution = []
        for crom in newGen:
            solution.append((fitness(crom[0], crom[1]), crom))
        solution.sort()
        if(bestSolution[0] > solution[0][0]):
            bestSolution = solution[0]
    return bestSolution

if __name__ == '__main__':
    pop_size = 10
    total_gen = 100
    mutate_percent = 10
    population = generatePop(pop_size)
    best_sol = geneticAlgo(population, total_gen, mutate_percent)
    print(best_sol)