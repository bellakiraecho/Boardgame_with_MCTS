import sys
from tictactoe import TicTacToe
from mcts import MCTS

def main(game_mode=None):
    if game_mode is None:
        game_mode = input("Enter 0 for player vs AI, 1 for player vs player, or 2 for AI vs AI: ")

    game = TicTacToe()
    if game_mode == "0":
        mcts = MCTS(game, time_limit=0.1)
        play_vs_ai(game, mcts)
    elif game_mode == "1":
        play_vs_player(game)
    elif game_mode == "2":
        mcts1 = MCTS(game, time_limit=0.1)
        mcts2 = MCTS(game, time_limit=0.1)
        result, game_log = play_ai_vs_ai(game, mcts1, mcts2, log_game=True, print_board=True)
        print(game_log.strip())
    else:
        print("Invalid input. Please enter 0, 1, or 2.")
        main()

def play_vs_ai(game, mcts):
    while not game.is_game_over():
        game.print_board()
        if game.current_player == "X":
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if not game.make_move(row, col):
                print("Invalid move. Try again.")
        else:
            row, col = mcts.run()
            game.make_move(row, col)

    game.print_board()
    if game.current_winner:
        print(f"Player {game.current_winner} wins!")
    else:
        print("It's a draw!")

def play_vs_player(game):
    while not game.is_game_over():
        game.print_board()
        row = int(input(f"Player {game.current_player}, enter the row (0, 1, or 2): "))
        col = int(input(f"Player {game.current_player}, enter the column (0, 1, or 2): "))
        if not game.make_move(row, col):
            print("Invalid move. Try again.")

    game.print_board()
    if game.current_winner:
        print(f"Player {game.current_winner} wins!")
    else:
        print("It's a draw!")

def play_ai_vs_ai(game, mcts1, mcts2, log_game=False, print_board=False):
    game_log = ""
    while not game.is_game_over():
        if log_game:
            game_log += get_board_log(game)
        if print_board:
            game.print_board()
        if game.current_player == "X":
            row, col = mcts1.run()
        else:
            row, col = mcts2.run()
        game.make_move(row, col)
    
    if log_game:
        game_log += get_board_log(game)
        if game.current_winner:
            game_log += f"Player {game.current_winner} wins!\n"
        else:
            game_log += "It's a draw!\n"
    
    return (game.current_winner, game_log)

def get_board_log(game):
    board_log = ""
    for row in game.board:
        board_log += "|".join(row) + "\n"
        board_log += "-" * 5 + "\n"
    board_log += "\n"
    return board_log

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
