import unittest, player, board

class TestBoardClass(unittest.TestCase):
    
    def test_valid_move(self):
        testBoard = board.Board()
        positions = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        turns = 8
        while turns > -1:
            self.assertTrue(testBoard.valid_move(positions[turns]))
            turns -= 1
            
    def test_invalid_move(self):
        testBoard = board.Board()
        symbol = "X"
        positions = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        turns = 8
        numPos = 8
        
        while numPos > -1:
            testBoard.change_board(positions[numPos], symbol)
            numPos -= 1
        
        while turns > -1:
            self.assertFalse(testBoard.valid_move(positions[turns]))
            turns -= 1
            
    def test_invalid_position(self):
        testBoard = board.Board()
        testPosition = "Q"
        
        self.assertFalse(testBoard.valid_move(testPosition))
            
    def test_horizontal_win_1(self):
        testBoard = board.Board()
        testPlayer = player.Player("X")
        
        testBoard.change_board("0", testPlayer.type)
        testBoard.change_board("1", testPlayer.type)
        testBoard.change_board("2", testPlayer.type)
        
        self.assertTrue(testBoard.check_win(testPlayer))
        
    def test_horizontal_win_2(self):
        testBoard = board.Board()
        testPlayer = player.Player("X")
        
        testBoard.change_board("3", testPlayer.type)
        testBoard.change_board("4", testPlayer.type)
        testBoard.change_board("5", testPlayer.type)
        
        self.assertTrue(testBoard.check_win(testPlayer))
        
    def test_horizontal_win_3(self):
        testBoard = board.Board()
        testPlayer = player.Player("X")
        
        testBoard.change_board("6", testPlayer.type)
        testBoard.change_board("7", testPlayer.type)
        testBoard.change_board("8", testPlayer.type)
        
        self.assertTrue(testBoard.check_win(testPlayer))
        
    def test_vertical_win_1(self):
        testBoard = board.Board()
        testPlayer = player.Player("X")
        
        testBoard.change_board("0", testPlayer.type)
        testBoard.change_board("3", testPlayer.type)
        testBoard.change_board("6", testPlayer.type)
        
        self.assertTrue(testBoard.check_win(testPlayer))
        
    def test_vertical_win_2(self):
        testBoard = board.Board()
        testPlayer = player.Player("X")
        
        testBoard.change_board("1", testPlayer.type)
        testBoard.change_board("4", testPlayer.type)
        testBoard.change_board("7", testPlayer.type)
        
        self.assertTrue(testBoard.check_win(testPlayer))
        
    def test_vertical_win_3(self):
        testBoard = board.Board()
        testPlayer = player.Player("X")
        
        testBoard.change_board("2", testPlayer.type)
        testBoard.change_board("5", testPlayer.type)
        testBoard.change_board("8", testPlayer.type)
        
        self.assertTrue(testBoard.check_win(testPlayer))
        
    def test_diagonal_win_1(self):
        testBoard = board.Board()
        testPlayer = player.Player("X")
        
        testBoard.change_board("0", testPlayer.type)
        testBoard.change_board("4", testPlayer.type)
        testBoard.change_board("8", testPlayer.type)
        
        self.assertTrue(testBoard.check_win(testPlayer))
        
    def test_diagonal_win_2(self):
        testBoard = board.Board()
        testPlayer = player.Player("X")
        
        testBoard.change_board("2", testPlayer.type)
        testBoard.change_board("4", testPlayer.type)
        testBoard.change_board("6", testPlayer.type)
        
        self.assertTrue(testBoard.check_win(testPlayer))

    def test_no_win(self):
        testBoard = board.Board()
        testPlayer = player.Player("X")

        self.assertFalse(testBoard.check_win(testPlayer))
        
    def test_change_board_valid(self):
        testBoard = board.Board()
        symbol = "X"
        positions = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        numPos = 8
        
        while numPos > -1:
            self.assertTrue(testBoard.change_board(positions[numPos], symbol))
            numPos -= 1
            
    def test_change_board_invalid(self):
        testBoard = board.Board()
        symbol = "X"
        positions = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        turns = 8
        numPos = 8
        
        while numPos > -1:
            testBoard.change_board(positions[numPos], symbol)
            numPos -= 1
        
        while turns > -1:
            self.assertFalse(testBoard.change_board(positions[numPos], symbol))
            turns -= 1

if __name__ == '__main__':
    unittest.main()