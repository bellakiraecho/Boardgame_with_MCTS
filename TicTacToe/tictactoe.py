class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_winner = None
        self.current_player = "X"

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                self.current_winner = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def check_winner(self, row, col):
        board = self.board
        player = self.board[row][col]

        # Check row
        if all([cell == player for cell in board[row]]):
            return True
        # Check column
        if all([board[r][col] == player for r in range(3)]):
            return True
        # Check diagonals
        if row == col and all([board[i][i] == player for i in range(3)]):
            return True
        if row + col == 2 and all([board[i][2-i] == player for i in range(3)]):
            return True
        return False

    def get_empty_squares(self):
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == " "]

    def is_full(self):
        return all([cell != " " for row in self.board for cell in row])

    def is_game_over(self):
        return self.current_winner is not None or self.is_full()

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)
        print()


    def copy(self):
        new_game = TicTacToe()
        new_game.board = [row[:] for row in self.board]
        new_game.current_player = self.current_player
        new_game.current_winner = self.current_winner
        return new_game