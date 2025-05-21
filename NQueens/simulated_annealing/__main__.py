from random import randint, random
from math import exp

N = 4  # Board size


def configureRandomly(state):
    for i in range(N):
        state[i] = randint(0, N - 1)


def printBoard(state):
    for i in range(N):
        for j in range(N):
            print('Q' if state[j] == i else '_', end=' ')
        print()
    print()


def calculateObjective(state):
    attacking = 0
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j]:  # Same row
                attacking += 1
            elif abs(state[i] - state[j]) == abs(i - j):  # Same diagonal
                attacking += 1
    return attacking


def getRandomNeighbor(state):
    neighbor = state[:]
    col = randint(0, N - 1)
    newRow = randint(0, N - 1)
    while newRow == neighbor[col]:
        newRow = randint(0, N - 1)
    neighbor[col] = newRow
    return neighbor


def simulatedAnnealing():
    current = [0] * N
    configureRandomly(current)
    currentHeuristic = calculateObjective(current)
    temperature = 100.0
    coolingRate = 0.99
    iteration = 1

    while temperature > 0.1 and currentHeuristic > 0:
        neighbor = getRandomNeighbor(current)
        neighborHeuristic = calculateObjective(neighbor)
        delta = neighborHeuristic - currentHeuristic

        if delta < 0 or random() < exp(-delta / temperature):
            current = neighbor
            currentHeuristic = neighborHeuristic

        print(f"Iteration {iteration} | Heuristic: {currentHeuristic} | Temp: {temperature:.2f}")
        printBoard(current)
        temperature *= coolingRate
        iteration += 1

    print("Final State:")
    printBoard(current)
    print("Final Heuristic:", currentHeuristic)


if __name__ == "__main__":
    simulatedAnnealing()
