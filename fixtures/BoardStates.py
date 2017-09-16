emptyBoard = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
]

winDirectlyToRight = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [2, 2, 2, 0, 0, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
]

winDirectlyToRightNotBottomRow = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [2, 2, 1, 2, 2, 0, 0],
]

oneBlankTwoInRowStartingInColumn0 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [1, 0, 2, 0, 0, 0, 0],
  [1, 0, 1, 1, 2, 2, 2],
]

oneBlankTwoInRowStartingInColumn0_invalid = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [1, 0, 1, 1, 0, 0, 0],
  [1, 0, 2, 2, 1, 2, 2],
]

blankThreeInRow_invalid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 2, 2],
    [0, 0, 2, 2, 1, 2, 2],
]

threeInColumn0 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0],
  [1, 0, 2, 1, 2, 2, 2],
  [1, 0, 2, 2, 1, 2, 2],
]

threeInColumn1 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 0],
  [1, 1, 2, 1, 2, 2, 2],
  [1, 1, 2, 2, 1, 2, 2],
]
threeInColumn2 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0],
  [1, 0, 1, 1, 2, 2, 2],
  [1, 0, 1, 2, 1, 2, 2],
]
threeInColumn3 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0],
  [1, 0, 2, 1, 2, 2, 2],
  [1, 0, 2, 1, 1, 2, 2],
]
threeInColumn4 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 0, 2, 1, 1, 2, 2],
  [1, 0, 2, 2, 1, 2, 2],
]
threeInColumn5 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0],
  [1, 0, 2, 1, 1, 1, 2],
  [1, 0, 2, 2, 1, 1, 2],
]
threeInColumn6 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1],
  [1, 0, 2, 1, 2, 1, 1],
  [1, 0, 2, 2, 1, 1, 1],
]
threeInRightDiag0 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 2, 0, 0, 1],
  [2, 1, 2, 1, 2, 1, 1],
  [1, 2, 2, 2, 1, 1, 1],
]
threeInRightDiag1 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 2, 1, 2, 0, 1],
  [2, 1, 1, 1, 2, 1, 1],
  [1, 1, 2, 2, 1, 1, 1],
]
threeInRightDiag2 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 2, 2, 1, 2, 1],
  [2, 1, 1, 1, 2, 1, 1],
  [1, 1, 1, 2, 1, 1, 1],
]
threeInRightDiag3 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 2, 2, 1, 2],
  [2, 1, 0, 1, 1, 1, 2],
  [1, 1, 2, 1, 1, 1, 2],
]
# should be None
threeInRightDiag4 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 2, 2, 2, 1],
  [2, 1, 0, 1, 1, 1, 2],
  [1, 1, 2, 1, 1, 1, 1],
]
# should be None
threeInRightDiag3Row2 = [
  [0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 1, 2, 0],
  [0, 0, 0, 1, 2, 2, 0],
  [0, 0, 0, 2, 2, 1, 1],
  [2, 1, 0, 1, 1, 2, 2],
  [1, 1, 2, 1, 1, 1, 1],
]
oneBlankTwoInRightDiag0 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 2, 2, 0],
  [0, 0, 1, 2, 2, 1, 1],
  [2, 0, 2, 1, 1, 2, 2],
  [1, 1, 2, 1, 1, 1, 1],
]
oneBlankTwoInRightDiag1 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 2, 0],
  [0, 0, 0, 1, 2, 1, 1],
  [2, 0, 0, 2, 1, 2, 2],
  [1, 1, 2, 1, 1, 1, 2],
]
oneBlankTwoInRightDiag2 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 0],
  [0, 0, 0, 0, 1, 1, 1],
  [2, 0, 2, 0, 1, 2, 2],
  [1, 2, 1, 1, 2, 1, 1],
]
oneBlankTwoInRightDiag3 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 1, 1],
  [2, 0, 2, 0, 0, 2, 2],
  [1, 1, 2, 1, 1, 2, 2],
]
# should be None
oneBlankTwoInRightDiag4 = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 0, 1],
  [2, 0, 2, 0, 0, 0, 2],
  [1, 1, 2, 1, 1, 2, 2],
]
# should be None
oneBlankTwoInRightDiag3Row2 = [
  [0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 1, 2, 1, 1],
  [0, 0, 0, 2, 1, 2, 1],
  [2, 0, 2, 2, 1, 2, 2],
  [1, 1, 2, 1, 1, 2, 2],
]
