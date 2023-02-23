import unittest, player, tictactoe

class TestTicTacToeClass(unittest.TestCase):
    
    def test_switch_x_to_o(self):
        testTicTac = tictactoe.TicTacToe()
        testPlayer = testTicTac.player1
        testPlayer2 = player.Player("O")
        switchedPlayer = testTicTac.switch_turn(testPlayer)
        self.assertEqual(switchedPlayer.type, testPlayer2.type)
        
    def test_switch_o_to_x(self):
        testTicTac = tictactoe.TicTacToe()
        testPlayer = testTicTac.player2
        testPlayer1 = player.Player("X")
        switchedPlayer = testTicTac.switch_turn(testPlayer)
        self.assertEqual(switchedPlayer.type, testPlayer1.type)
        
    def test_modify_board_success(self):
        testTicTac = tictactoe.TicTacToe()
        testBoard = ["X", " ", " ",
                    " ", " ", " ",
                    " ", " ", " "]
        testPosition = "0"
        testSymbol = "X"
        turns = 0
        
        testTicTac.modify_board(testPosition, testSymbol)
        
        for key in testTicTac.board.board:
            self.assertEqual(testTicTac.board.board[key], testBoard[turns])
            turns += 1

    def test_modify_board_failure(self):
        testTicTac = tictactoe.TicTacToe()
        testBoard = ["X", " ", " ",
                    " ", " ", " ",
                    " ", " ", " "]
        testPosition = "0"
        testSymbol = "X"
        testSymbol2 = "O"
        turns = 0
        
        print("Please type in '0' for the purposes of testing board modification failure.")
        
        testTicTac.modify_board(testPosition, testSymbol)
        
        testTicTac.modify_board(testPosition, testSymbol2)
        
        for key in testTicTac.board.board:
            self.assertEqual(testTicTac.board.board[key], testBoard[turns])
            turns += 1
        
if __name__ == '__main__':
    unittest.main()