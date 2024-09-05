# A simple Othello game and MCTS AI

game.py is the game itself
mcts.py is the MCTS ai file
main.py is the file which run the game
simulate.py is to simulate the win count

# Requirements

python 3.x
VSC(recommend, see reason in the Addition part)

# Setting
In main.py at line 36, 67 and 68 which look like
# ai = MCTS(game, time_limit=0.1)
Is the code for set the time limit for AI during the game
change the number of time_limit=0.1 to set different time limit
for example, try time_limit=1 or time_limit=0.01
Line 36 for player vs AI round's AI
Line 67 and 68 for AI vs AI round's AI also for simulate

# How to run:

# 1 For single round:
1. Run the main.py
2. Then the terminal will show:
    Welcome to Othello!
    1. Player vs Player
    2. Player vs AI
    3. AI vs AI
    Select game mode: 
3. Enter the number of which mode want to run in terminal
4. Enjoy the game
5. Addition for human player: Enter row and column at the same time (e.g., 3 4):

# 2 For simulate:
1. Run the simulate.py
2. Then the terminal will show "Enter the number of games to simulate: "
3. Enter the number of how many round want to test for AI vs AI
4. It will show all game during the simulate and print the number of each AI player when it is done

# Addition
I was build this game on VSC, and seems like run by python directly,
the game will shut down immediately after the game is over 
which means it can't view the result.