from random import randint

N = 4  # Size of the board


def configureRandomly(board, state):
    for i in range(N):
        state[i] = randint(0, 100000) % N
        board[state[i]][i] = 1


def printBoard(board):
    for i in range(N):
        print(*board[i])
    print()


def printState(state):
    print("State:", *state)
    print()


def compareStates(state1, state2):
    for i in range(N):
        if state1[i] != state2[i]:
            return False
    return True


def fill(board, value):
    for i in range(N):
        for j in range(N):
            board[i][j] = value


def calculateObjective(board, state):
    attacking = 0
    for i in range(N):
        row = state[i]

        # Left
        col = i - 1
        while col >= 0 and board[row][col] != 1:
            col -= 1
        if col >= 0 and board[row][col] == 1:
            attacking += 1

        # Right
        col = i + 1
        while col < N and board[row][col] != 1:
            col += 1
        if col < N and board[row][col] == 1:
            attacking += 1

        # Diagonal Left Up
        row = state[i] - 1
        col = i - 1
        while row >= 0 and col >= 0 and board[row][col] != 1:
            row -= 1
            col -= 1
        if row >= 0 and col >= 0 and board[row][col] == 1:
            attacking += 1

        # Diagonal Right Down
        row = state[i] + 1
        col = i + 1
        while row < N and col < N and board[row][col] != 1:
            row += 1
            col += 1
        if row < N and col < N and board[row][col] == 1:
            attacking += 1

        # Diagonal Left Down
        row = state[i] + 1
        col = i - 1
        while row < N and col >= 0 and board[row][col] != 1:
            row += 1
            col -= 1
        if row < N and col >= 0 and board[row][col] == 1:
            attacking += 1

        # Diagonal Right Up
        row = state[i] - 1
        col = i + 1
        while row >= 0 and col < N and board[row][col] != 1:
            row -= 1
            col += 1
        if row >= 0 and col < N and board[row][col] == 1:
            attacking += 1

    return int(attacking / 2)


def generateBoard(board, state):
    fill(board, 0)
    for i in range(N):
        board[state[i]][i] = 1


def copyState(state1, state2):
    for i in range(N):
        state1[i] = state2[i]


def getNeighbour(board, state):
    opBoard = [[0 for _ in range(N)] for _ in range(N)]
    opState = [0 for _ in range(N)]
    copyState(opState, state)
    generateBoard(opBoard, opState)
    opObjective = calculateObjective(opBoard, opState)

    neighbourBoard = [[0 for _ in range(N)] for _ in range(N)]
    neighbourState = [0 for _ in range(N)]
    copyState(neighbourState, state)
    generateBoard(neighbourBoard, neighbourState)

    for i in range(N):
        for j in range(N):
            if j != state[i]:
                neighbourState[i] = j
                neighbourBoard[j][i] = 1
                neighbourBoard[state[i]][i] = 0

                temp = calculateObjective(neighbourBoard, neighbourState)

                if temp <= opObjective:
                    opObjective = temp
                    copyState(opState, neighbourState)
                    generateBoard(opBoard, opState)

                neighbourBoard[j][i] = 0
                neighbourState[i] = state[i]
                neighbourBoard[state[i]][i] = 1

    copyState(state, opState)
    fill(board, 0)
    generateBoard(board, state)


def hillClimbing(board, state):
    neighbourBoard = [[0 for _ in range(N)] for _ in range(N)]
    neighbourState = [0 for _ in range(N)]

    copyState(neighbourState, state)
    generateBoard(neighbourBoard, neighbourState)

    iteration = 0
    while True:
        copyState(state, neighbourState)
        generateBoard(board, state)

        currentHeuristic = calculateObjective(board, state)
        print(f"\nIteration {iteration}")
        print("Board:")
        printBoard(board)
        print("State:", state)
        print("Heuristic (attacking pairs):", currentHeuristic)

        getNeighbour(neighbourBoard, neighbourState)

        newHeuristic = calculateObjective(neighbourBoard, neighbourState)
        if compareStates(state, neighbourState):
            print("\nFinal Board (Local Minima or Solution):")
            printBoard(board)
            print("Final State:", state)
            print("Final Heuristic:", currentHeuristic)
            break
        elif currentHeuristic == newHeuristic:
            neighbourState[randint(0, N - 1)] = randint(0, N - 1)
            generateBoard(neighbourBoard, neighbourState)

        iteration += 1


# Driver code
state = [0] * N
board = [[0 for _ in range(N)] for _ in range(N)]

configureRandomly(board, state)
print("Initial Board:")
printState(state)
printBoard(board)

hillClimbing(board, state)
