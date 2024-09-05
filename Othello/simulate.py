from main import ai_vs_ai
from game import Othello

def simulate_games(num_games):
    black_wins = 0
    white_wins = 0
    draws = 0

    for _ in range(num_games):
        game = Othello()
        result = ai_vs_ai(game)

        if result == 1:
            black_wins += 1
        elif result == -1:
            white_wins += 1
        else:
            draws += 1

    print(f"Total games: {num_games}")
    print(f"Black wins: {black_wins}")
    print(f"White wins: {white_wins}")
    print(f"Draws: {draws}")

if __name__ == "__main__":
    try:
        num_games = int(input("Enter the number of games to simulate: "))
        simulate_games(num_games)
    except ValueError:
        print("Please enter a valid integer.")
