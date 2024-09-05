import subprocess

def run_simulation(num_games):
    ai1_wins = 0
    ai2_wins = 0
    draws = 0

    for i in range(num_games):
        process = subprocess.Popen(
            ["python", "main.py", "2"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()
        output = stdout.strip()  # Use strip() to avoid double newlines
        
        if "Player X wins!" in output:
            ai1_wins += 1
            print(f"Non-Draw Round {i + 1}")
            print(output)
        elif "Player O wins!" in output:
            ai2_wins += 1
            print(f"Non-Draw Round {i + 1}")
            print(output)
        elif "It's a draw!" in output:
            draws += 1

    print(f"AI 1 (X) wins: {ai1_wins}")
    print(f"AI 2 (O) wins: {ai2_wins}")
    print(f"Draws: {draws}")

if __name__ == "__main__":
    num_games = int(input("Enter the number of games to simulate: "))
    run_simulation(num_games)
