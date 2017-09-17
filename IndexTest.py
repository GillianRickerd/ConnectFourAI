import unittest
from index import Index
import sys
sys.path.insert(0, './fixtures')
from fixtures import BoardStates
from fixtures import Rows

class IndexTest(unittest.TestCase):
  @unittest.skip("implement later")
  def test_winInOnePlay(self):
    """win with opening to the right"""
    # TODO: add all win in one play cases
    # x = Index.winInOnePlay(1, BoardStates.winDirectlyToRight)
    # self.assertEqual(x, 3)

  def test_firstTurnInMiddle(self):
    """if this is the first move, play in the center column"""
    play = Index.playFirstTurn(1, BoardStates.emptyBoard)
    self.assertEqual(play, 3)

  def test_threeInARow(self):
    """returns the column number if there are three in a row with one open to the right"""
    play = Index.threeInARow(1, 0, Rows.threeInARowStartingInColumn0)
    self.assertEqual(play, 3)
    play2 = Index.threeInARow(1, 1, Rows.threeInARowStartingInColumn1)
    self.assertEqual(play2, 4)
    play3 = Index.threeInARow(1, 2, Rows.threeInARowStartingInColumn2)
    self.assertEqual(play3, 5)
    play4 = Index.threeInARow(1, 3, Rows.threeInARowStartingInColumn3)
    self.assertEqual(play4, 6)
    # TODO: three in a row if not bottom row

  def test_oneBlankTwoInRow(self):
    """returns the column number for the open spot if there is one then a blank spot then two in a row"""
    play = Index.oneBlankTwoInRow(1, 0, Rows.oneBlankTwoInRowStartingInColumn0)
    self.assertEqual(play, 1)
    play2 = Index.oneBlankTwoInRow(1, 1, Rows.oneBlankTwoInRowStartingInColumn1)
    self.assertEqual(play2, 2)
    play3 = Index.oneBlankTwoInRow(1, 2, Rows.oneBlankTwoInRowStartingInColumn2)
    self.assertEqual(play3, 3)
    play4 = Index.oneBlankTwoInRow(1, 3, Rows.oneBlankTwoInRowStartingInColumn3)
    self.assertEqual(play4, 4)

  def test_oneBlankTwoInRow_winInOnePlay(self):
    """returns the open spot if there is one then blank then two when the open space is not the bottom row"""
    play = Index.winInOnePlay(1, BoardStates.oneBlankTwoInRowStartingInColumn0)
    self.assertEqual(play, 1)
    play2 = Index.winInOnePlay(1, BoardStates.oneBlankTwoInRowStartingInColumn0_invalid)
    self.assertIsNone(play2)

  def test_twoBlankOneInRow(self):
    """returns the open spot when there are two in a row, then a blank space, then one"""
    play = Index.twoBlankOneInRow(1, 0, Rows.twoBlankOneInRowStartingInColumn0)
    self.assertEqual(play, 2)
    play2 = Index.twoBlankOneInRow(1, 1, Rows.twoBlankOneInRowStartingInColumn1)
    self.assertEqual(play2, 3)
    play3 = Index.twoBlankOneInRow(1, 2, Rows.twoBlankOneInRowStartingInColumn2)
    self.assertEqual(play3, 4)
    play4 = Index.twoBlankOneInRow(1, 3, Rows.twoBlankOneInRowStartingInColumn3)
    self.assertEqual(play4, 5)
    # TODO: two blank one in row not bottom row

  def test_blankThreeInRow(self):
    """returns the open column if there is a blank then three in a row"""
    play = Index.blankThreeInRow(1, 0, Rows.blankThreeInRowStartingInColumn0)
    self.assertEqual(play, 0)
    play2 = Index.blankThreeInRow(1, 1, Rows.blankThreeInRowStartingInColumn1)
    self.assertEqual(play2, 1)
    play3 = Index.blankThreeInRow(1, 2, Rows.blankThreeInRowStartingInColumn2)
    self.assertEqual(play3, 2)
    play4 = Index.blankThreeInRow(1, 3, Rows.blankThreeInRowStartingInColumn3)
    self.assertEqual(play4, 3)
    playOnBoard = Index.winInOnePlay(1, BoardStates.blankThreeInRow_invalid)
    self.assertIsNone(playOnBoard)

  def test_threeInColumn(self):
    """returns the open column if there is a column with three in a row"""
    play = Index.threeInColumn(1, 0, 5, BoardStates.threeInColumn0)
    self.assertEqual(play, 0)
    play = Index.threeInColumn(1, 1, 5, BoardStates.threeInColumn1)
    self.assertEqual(play, 1)
    play = Index.threeInColumn(1, 2, 5, BoardStates.threeInColumn2)
    self.assertEqual(play, 2)
    play = Index.threeInColumn(1, 3, 5, BoardStates.threeInColumn3)
    self.assertEqual(play, 3)
    play = Index.threeInColumn(1, 4, 5, BoardStates.threeInColumn4)
    self.assertEqual(play, 4)
    play = Index.threeInColumn(1, 5, 5, BoardStates.threeInColumn5)
    self.assertEqual(play, 5)
    play = Index.threeInColumn(1, 6, 5, BoardStates.threeInColumn6)
    self.assertEqual(play, 6)

  def test_threeInRightDiag(self):
    """returns the open column if there are three in a row
      up and to the right"""
    play = Index.threeInRightDiag(1, 0, 5, BoardStates.threeInRightDiag0)
    self.assertEqual(play, 3)
    play2 = Index.threeInRightDiag(1, 1, 5, BoardStates.threeInRightDiag1)
    self.assertEqual(play2, 4)
    play3 = Index.threeInRightDiag(1, 2, 5, BoardStates.threeInRightDiag2)
    self.assertEqual(play3, 5)
    play4 = Index.threeInRightDiag(1, 3, 5, BoardStates.threeInRightDiag3)
    self.assertEqual(play4, 6)
    # Should return None because 4 in a row won't be possible
    play5 = Index.threeInRightDiag(1, 4, 5, BoardStates.threeInRightDiag4)
    self.assertIsNone(play5)
    play6 = Index.threeInRightDiag(1, 3, 2, BoardStates.threeInRightDiag3Row2)
    self.assertIsNone(play6)

  def test_oneBlankTwoInRightDiag(self):
    """returns the open column if there's one then blank then two
      in the diag up and to the right"""
    play = Index.oneBlankTwoInRightDiag(1, 0, 5, BoardStates.oneBlankTwoInRightDiag0)
    self.assertEqual(play, 1)
    play2 = Index.oneBlankTwoInRightDiag(1, 1, 5, BoardStates.oneBlankTwoInRightDiag1)
    self.assertEqual(play2, 2)
    play3 = Index.oneBlankTwoInRightDiag(1, 2, 5, BoardStates.oneBlankTwoInRightDiag2)
    self.assertEqual(play3, 3)
    play4 = Index.oneBlankTwoInRightDiag(1, 3, 5, BoardStates.oneBlankTwoInRightDiag3)
    self.assertEqual(play4, 4)
    # should return None
    play5 = Index.oneBlankTwoInRightDiag(1, 4, 5, BoardStates.oneBlankTwoInRightDiag4)
    self.assertIsNone(play5)
    play6 = Index.oneBlankTwoInRightDiag(1, 3, 2, BoardStates.oneBlankTwoInRightDiag3Row2)
    self.assertIsNone(play6)

  def test_twoBlankOneInRightDiag(self):
    """returns the open column if there's two then blank then
    one in the diag up and to the right"""
    play = Index.twoBlankOneInRightDiag(1, 0, 5, BoardStates.twoBlankOneInRightDiag0)
    self.assertEqual(play, 2)
    play2 = Index.twoBlankOneInRightDiag(1, 1, 5, BoardStates.twoBlankOneInRightDiag1)
    self.assertEqual(play2, 3)
    play3 = Index.twoBlankOneInRightDiag(1, 2, 5, BoardStates.twoBlankOneInRightDiag2)
    self.assertEqual(play3, 4)
    play4 = Index.twoBlankOneInRightDiag(1, 3, 5, BoardStates.twoBlankOneInRightDiag3)
    self.assertEqual(play4, 5)
    # should return None
    play5 = Index.twoBlankOneInRightDiag(1, 4, 5, BoardStates.twoBlankOneInRightDiag4)
    self.assertIsNone(play5)
    play6 = Index.twoBlankOneInRightDiag(1, 3, 2, BoardStates.twoBlankOneInRightDiag3Row2)
    self.assertIsNone(play6)

  # TODO: diagonals up to right
  # TODO: diagonals down to right
    # TODO: construct diagonal and column methods???
  # TODO: 2 in a row
    # rows
    # column
    # diagonals up to right
    # diagonals up to left

if __name__ == '__main__':
  unittest.main()
