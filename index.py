class Index:

    def winInOnePlay(playerNumber, boardStateAfterOpponent):
        for row in range(5, -1, -1):
            for column in range(7):
                possiblePlay1 = Index.threeInARow(playerNumber, column, boardStateAfterOpponent[row])
                if bool(possiblePlay1) and row < 5:
                    if boardStateAfterOpponent[row + 1][possiblePlay1] != 0:
                        return possiblePlay1
                elif bool(possiblePlay1):
                    return possiblePlay1
                possiblePlay2 = Index.oneBlankTwoInRow(playerNumber, column, boardStateAfterOpponent[row])
                if bool(possiblePlay2) and row < 5:
                    if boardStateAfterOpponent[row + 1][possiblePlay2] != 0:
                        return possiblePlay2
                elif bool(possiblePlay2):
                    return possiblePlay2

    def playFirstTurn(playerNumber, boardState):
        if boardState[0][3] == 0:
            return 3

    def threeInARow(playerNumber, columnNumber, rowState):
        if rowState[columnNumber] == playerNumber and rowState[columnNumber + 1] == playerNumber and rowState[columnNumber + 2] == playerNumber and rowState[columnNumber + 3] == 0:
            return columnNumber + 3

    def oneBlankTwoInRow(playerNumber, columnNumber, rowState):
        if rowState[columnNumber] == playerNumber and rowState[columnNumber + 1] == 0 and rowState[columnNumber + 2] == playerNumber and rowState[columnNumber + 3] == playerNumber:
            return columnNumber + 1

    def twoBlankOneInRow(playerNumber, columnNumber, rowState):
        if rowState[columnNumber] == playerNumber and rowState[columnNumber + 1] == playerNumber and rowState[columnNumber + 2] == 0 and rowState[columnNumber + 3] == playerNumber:
            return columnNumber + 2

    def blankThreeInRow(playerNumber, columnNumber, rowState):
        if rowState[columnNumber] == 0 and rowState[columnNumber + 1] == playerNumber and rowState[columnNumber + 2] == playerNumber and rowState[columnNumber + 3] == playerNumber:
            return columnNumber


