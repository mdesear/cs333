import tictactoe

def play_game():
    tictac = tictactoe.TicTacToe()
    tictac.print_valid_moves()
    player = tictactoe.player1
    turns = 9
    while turns > 0:
        turns -= 1
        tictac.print_board()
        position = input(f"{player.__str__()}, enter the number of the position you'd like to choose. ")
        tictac.modify_board(position, player.type)
        if tictac.game_win(player):
            tictac.print_board()
            print(f"{player.__str__()} is the winner!")
            break
        else: 
            player = tictac.switch_turn(player)
    if turns == 0:
        print("It's a tie! Game over!")

def main():
    play_game()
if __name__ == "__main__":
    main()