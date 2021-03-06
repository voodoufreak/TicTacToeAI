# Values for outcomes
scoreVals = {
    "X": -1,
    "O": 1,
    "tie": 0
}


# Finds the best move and plays such move
def bestMove(inputBoard):
    bestScore = float("-inf")
    for x in range(1, 10):
        if inputBoard.checkIfEmpty(x) == True:
            cordX, cordY = inputBoard.getCords(x)

            inputBoard.board[cordX, cordY] = "O"
            score = minimax(inputBoard, 0, False)
            inputBoard.board[cordX, cordY] = " "

            if score > bestScore:
                bestScore = score
                bestMove = [cordX, cordY]
    inputBoard.board[bestMove[0], bestMove[1]] = "O"


# Algo to find the best move
def minimax(inputBoard, depth, isMaximize):
    result = inputBoard.checkWin()

    if(result != None):
        return scoreVals[result]
    # Maxamize the AI
    if(isMaximize):
        bestScore = float("-inf")

        # Going through all possible moves
        for x in range(1, 10):
            if inputBoard.checkIfEmpty(x) == True:
                cordX, cordY = inputBoard.getCords(x)
                inputBoard.board[cordX, cordY] = "O"
                score = minimax(inputBoard, depth+1, False)
                inputBoard.board[cordX, cordY] = " "
                bestScore = max(score, bestScore)
        return bestScore
    else:
        # Minimize player
        bestScore = float("inf")

        # Going through all possible moves
        for x in range(1, 10):
            if inputBoard.checkIfEmpty(x) == True:
                cordX, cordY = inputBoard.getCords(x)
                inputBoard.board[cordX, cordY] = "X"
                score = minimax(inputBoard, depth+1, True)
                inputBoard.board[cordX, cordY] = " "
                bestScore = min(score, bestScore)
        return bestScore
