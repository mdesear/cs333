import player, board

class TicTacToe:
    def __init__(self):
        self.player1 = player.Player("X")
        self.player2 = player.Player("O")
        self.board = board.Board()

    def print_valid_moves(self):
        print("0 = Top Left\t\t1 = Top Middle\t\t2 = Top Right")
        print("3 = Middle Left\t\t4 = Center\t\t5 = Middle Right")
        print("6 = Bottom Left\t\t7 = Bottom Middle\t8 = Bottom Right\n")

    def print_board(self):
        self.board.print_board()

    def switch_turn(self, player):
        if player is self.player1:
            return self.player2
        else:
            return self.player1

    def game_win(self, player):
        return self.board.check_win(player)

    def modify_board(self, position, symbol):
        if self.board.change_board(position, symbol) is not None:
            return self.board.change_board(position, symbol)
        else:
            position = input("Not a valid position. Please try again. ")
            return self.board.change_board(position, symbol)
