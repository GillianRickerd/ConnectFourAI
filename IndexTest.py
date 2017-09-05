import unittest
from index import Index
import sys
sys.path.insert(0, './fixtures')
from fixtures import BoardStates
from fixtures import Rows

class IndexTest(unittest.TestCase):
    def test_winInOnePlay(self):
        """win with opening to the right"""
        # TODO: add all win in one play cases
        # 1110
        x = Index.winInOnePlay(1, BoardStates.winDirectlyToRight)
        self.assertEqual(x, 3)

    def test_firstTurnInMiddle(self):
        """if this is the first move, play in the center column"""
        play = Index.playFirstTurn(1, BoardStates.emptyBoard)
        self.assertEqual(play, 3)

    def test_threeInARow(self):
        """returns the column number if there are three in a row with one open to the right"""
        # 1110
        # params: playerNumber, columnNumber, row
        play = Index.threeInARow(1, 0, Rows.threeInARowStartingInColumn0)
        self.assertEqual(play, 3)
        play2 = Index.threeInARow(1, 1, Rows.threeInARowStartingInColumn1)
        self.assertEqual(play2, 4)
        play3 = Index.threeInARow(1, 2, Rows.threeInARowStartingInColumn2)
        self.assertEqual(play3, 5)
        play4 = Index.threeInARow(1, 3, Rows.threeInARowStartingInColumn3)
        self.assertEqual(play4, 6)

    def test_oneBlankTwoInRow(self):
        """returns the column number for the open spot if there is one then a blank spot then two in a row"""
        # 1011
        # params: playerNumber, columnNumber, row
        play = Index.oneBlankTwoInRow(1, 0, Rows.oneBlankTwoInRowStartingInColumn0)
        self.assertEqual(play, 1)
        play2 = Index.oneBlankTwoInRow(1, 1, Rows.oneBlankTwoInRowStartingInColumn1)
        self.assertEqual(play2, 2)
        play3 = Index.oneBlankTwoInRow(1, 2, Rows.oneBlankTwoInRowStartingInColumn2)
        self.assertEqual(play3, 3)
        play4 = Index.oneBlankTwoInRow(1, 3, Rows.oneBlankTwoInRowStartingInColumn3)
        self.assertEqual(play4, 4)

    def test_winInOnePlay_notBottom(self):
        """takes move to right only if the spot below it is filled"""
        # 1110
        # XXXX
        # TODO: add an assertion that checks that nothing is returned if that space is not valid
        # TODO: add all cases for win in one play
        play = Index.winInOnePlay(1, BoardStates.winDirectlyToRightNotBottomRow)
        self.assertEqual(play, 3)

    def test_oneBlankTwoInRow_winInOnePlay(self):
        # 1011
        # XXXX
        """returns the open spot if there is one then blank then two when the open space is not the bottom row"""
        play = Index.winInOnePlay(1, BoardStates.oneBlankTwoInRowStartingInColumn0)
        self.assertEqual(play, 1)
        play2 = Index.winInOnePlay(1, BoardStates.oneBlankTwoInRowStartingInColumn0_invalid)
        self.assertIsNone(play2)

    def test_twoBlankOneInRow(self):
        # 1101
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
        # 0111
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

    # TODO: column
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
