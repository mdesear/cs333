class Board:
    def __init__(self):
        self.board = {"0":" ", "1":" ", "2":" ",
                    "3":" ", "4":" ", "5":" ",
                    "6":" ", "7":" ", "8":" "}

    def print_board(self):
        print(self.board["0"] + "|" + self.board["1"] + "|" + self.board["2"])
        print("-+-+-")
        print(self.board["3"] + "|" + self.board["4"] + "|" + self.board["5"])
        print("-+-+-")
        print(self.board["6"] + "|" + self.board["7"] + "|" + self.board["8"])

    def valid_move(self, position):
        try:
            if self.board[position] == " ":
                return True
        except: 
            return False
        return False

    def check_win(self, player):
        symbol = player.type
        wins = [
            # Horizontal
            ["0", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "8"],
            # Vertical
            ["0", "3", "6"],
            ["1", "4", "7"],
            ["2", "5", "8"],
            # Diagonal
            ["0", "4", "8"],
            ["2", "4", "6"]
        ]
        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] == symbol:
                return True
        return False

    def change_board(self, position, symbol):
        if self.valid_move(position):
            self.board[position] = symbol
            return self.board
        return None