from game import Othello
from mcts import MCTS


def display_game_result(game):
    game.print_board()
    black_score, white_score = game.get_score()
    print(f"Game over! Final score -> Black (●): {black_score}, White (○): {white_score}")
    if black_score > white_score:
        print("Black wins!")
    elif white_score > black_score:
        print("White wins!")
    else:
        print("It's a tie!")

def player_vs_player():
    game = Othello()
    while not game.is_game_over():
        game.print_board()
        if game.has_valid_moves(game.current_player):
            print(f"Current Player: {'Black (●)' if game.current_player == 1 else 'White (○)'}")
            try:
                row, col = map(int, input("Enter row and column (e.g., 3 4): ").split())
                game.make_move(row, col, game.current_player)
            except ValueError:
                print("Invalid input. Please enter two numbers separated by space.")
        else:
            print(f"No valid moves for {'Black (●)' if game.current_player == 1 else 'White (○)'}")
            if game.skip_turn():
                break

    display_game_result(game)

def player_vs_ai():
    game = Othello()
    ai = MCTS(time_limit=1.0)

    while not game.is_game_over():
        game.print_board()
        if game.current_player == 1:
            print("Your turn (Black ●)")
            if game.has_valid_moves(1):
                try:
                    row, col = map(int, input("Enter row and column (e.g., 3 4): ").split())
                    game.make_move(row, col, 1)
                except ValueError:
                    print("Invalid input. Please enter two numbers separated by space.")
            else:
                print("No valid moves for Black (●)")
                if game.skip_turn():
                    break
        else:
            print("AI's turn (White ○)")
            if game.has_valid_moves(-1):
                move = ai.get_best_move(game)
                game.make_move(move[0], move[1], -1)
            else:
                print("No valid moves for White (○)")
                if game.skip_turn():
                    break

    display_game_result(game)

def ai_vs_ai(game=None):
    if game is None:
        game = Othello()
    ai1 = MCTS(time_limit=0.0001)
    ai2 = MCTS(time_limit=0.0001)

    while not game.is_game_over():
        game.print_board()
        if game.has_valid_moves(game.current_player):
            if game.current_player == 1:
                print("AI 1's turn (Black ●)")
                move = ai1.get_best_move(game)
            else:
                print("AI 2's turn (White ○)")
                move = ai2.get_best_move(game)

            game.make_move(move[0], move[1], game.current_player)
        else:
            print(f"No valid moves for {'Black (●)' if game.current_player == 1 else 'White (○)'}")
            if game.skip_turn():
                break

    display_game_result(game)
    
    return game.get_winner()



def main():
    print("Welcome to Othello!")
    print("1. Player vs Player")
    print("2. Player vs AI")
    print("3. AI vs AI")
    choice = input("Select game mode: ")

    if choice == '1':
        player_vs_player()
    elif choice == '2':
        player_vs_ai()
    elif choice == '3':
        ai_vs_ai()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
