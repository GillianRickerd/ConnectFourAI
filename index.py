class Index:

  def winInOnePlay(playerNumber, boardStateAfterOpponent):
    for row in reversed(range(6)):
      for column in range(7):
        row_contents = boardStateAfterOpponent[row]
        three_in_row = Index.threeInARow(playerNumber, column, row_contents)
        if bool(three_in_row):
          if row < 5 and Index.is_valid_play(boardStateAfterOpponent, row, three_in_row):
            return three_in_row
          elif row is 5:
            return three_in_row
        one_blank_two = Index.oneBlankTwoInRow(playerNumber, column, row_contents)
        if bool(one_blank_two):
          if row < 5 and Index.is_valid_play(boardStateAfterOpponent, row, one_blank_two):
            return one_blank_two
          elif row is 5:
            return one_blank_two
        two_blank_one = Index.twoBlankOneInRow(playerNumber, column, row_contents)
        if bool(two_blank_one):
          if row < 5 and Index.is_valid_play(boardStateAfterOpponent, row, two_blank_one):
            return two_blank_one
          elif row is 5:
            return two_blank_one
        blank_three = Index.blankThreeInRow(playerNumber, column, row_contents)
        if bool(blank_three):
          if row < 5 and Index.is_valid_play(boardStateAfterOpponent, row, blank_three):
            return blank_three
          elif row is 5:
            return blank_three

  def playFirstTurn(playerNumber, boardState):
    if boardState[0][3] == 0:
      return 3

  def is_valid_play(board_state, row, column):
    if board_state[row + 1][column] != 0:
      return True

  def threeInARow(playerNumber, columnNumber, rowState):
    if rowState[columnNumber] == playerNumber and rowState[columnNumber + 1] == playerNumber and rowState[
    columnNumber + 2] == playerNumber and rowState[columnNumber + 3] == 0:
      return columnNumber + 3

  def oneBlankTwoInRow(playerNumber, columnNumber, rowState):
    if columnNumber <= 4 and rowState[columnNumber] == playerNumber and rowState[columnNumber + 1] == 0 and rowState[
    columnNumber + 2] == playerNumber and rowState[columnNumber + 3] == playerNumber:
      return columnNumber + 1

  def twoBlankOneInRow(playerNumber, columnNumber, rowState):
    if columnNumber <= 5 and rowState[columnNumber] == playerNumber and rowState[columnNumber + 1] == playerNumber and rowState[
    columnNumber + 2] == 0 and rowState[columnNumber + 3] == playerNumber:
      return columnNumber + 2

  def blankThreeInRow(playerNumber, columnNumber, rowState):
    if columnNumber <= 3 and rowState[columnNumber] == 0 and rowState[columnNumber + 1] == playerNumber and rowState[
    columnNumber + 2] == playerNumber and rowState[columnNumber + 3] == playerNumber:
      return columnNumber

  def threeInColumn(playerNumber, columnNumber, row, boardState):
    if row >= 3 and boardState[row][columnNumber] == playerNumber and boardState[row - 1][columnNumber] == playerNumber and boardState[
    row - 2][columnNumber] == playerNumber and boardState[row - 3][columnNumber] == 0:
      return columnNumber

  def threeInRightDiag(playerNumber, columnNumber, row, boardState):
    if columnNumber <= 3 and row >= 3 and boardState[row][columnNumber] == playerNumber and boardState[
    row - 1][columnNumber + 1] == playerNumber and boardState[row - 2][columnNumber + 2] == playerNumber and boardState[
    row - 3][columnNumber + 3] == 0 and boardState[row - 2][columnNumber + 3] != 0:
      return columnNumber + 3

  def oneBlankTwoInRightDiag(playerNumber, columnNumber, row, boardState):
    if columnNumber <= 3 and row >= 3 and boardState[row][columnNumber] == playerNumber and boardState[
    row - 1][columnNumber + 1] == 0 and boardState[row - 2][columnNumber + 2] == playerNumber and boardState[
    row - 3][columnNumber + 3] == playerNumber and boardState[row][columnNumber + 1] != 0:
      return columnNumber + 1

  def twoBlankOneInRightDiag(playerNumber, columnNumber, row, boardState):
    if columnNumber <= 3 and row >= 3 and boardState[row][columnNumber] == playerNumber and boardState[
        row - 1][columnNumber + 1] == playerNumber and boardState[row - 2][columnNumber + 2] == 0 and boardState[
        row - 3][columnNumber + 3] == playerNumber and boardState[row][columnNumber + 1] != 0:
      return columnNumber + 2

