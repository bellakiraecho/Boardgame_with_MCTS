class Othello:
    def __init__(self):
        self.board = [[0] * 8 for _ in range(8)]
        self.board[3][3] = self.board[4][4] = -1  # White
        self.board[3][4] = self.board[4][3] = 1   # Black
        self.current_player = 1  # 1 for black，-1 white

    def print_board(self):
        print("  " + " ".join(map(str, range(8))))
        for i, row in enumerate(self.board):
            print(f"{i} " + " ".join(self.symbol(x) for x in row))

    def symbol(self, x):
        return '●' if x == 1 else '○' if x == -1 else '.'

    def is_valid_move(self, row, col, player):
        if self.board[row][col] != 0:
            return False
        opponent = -player
        valid = False
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            found_opponent = False
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opponent:
                r += dr
                c += dc
                found_opponent = True
            if found_opponent and 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == player:
                valid = True
        return valid

    def make_move(self, row, col, player):
        if not self.is_valid_move(row, col, player):
            return False
        opponent = -player
        self.board[row][col] = player
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            to_flip = []
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opponent:
                to_flip.append((r, c))
                r += dr
                c += dc
            if to_flip and 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == player:
                for fr, fc in to_flip:
                    self.board[fr][fc] = player
        self.current_player = -self.current_player
        return True

    def has_valid_moves(self, player):
        return any(self.is_valid_move(row, col, player) for row in range(8) for col in range(8))

    def get_score(self):
        black_score = sum(row.count(1) for row in self.board)
        white_score = sum(row.count(-1) for row in self.board)
        return black_score, white_score

    def get_valid_moves(self, player):
        return [(row, col) for row in range(8) for col in range(8) if self.is_valid_move(row, col, player)]

    def is_game_over(self):
        return not self.has_valid_moves(1) and not self.has_valid_moves(-1)

    def get_winner(self):
        black_score, white_score = self.get_score()
        if black_score > white_score:
            return 1
        elif white_score > black_score:
            return -1
        else:
            return 0

    def clone(self):
        clone_game = Othello()
        clone_game.board = [row[:] for row in self.board]
        clone_game.current_player = self.current_player
        return clone_game

    def skip_turn(self):
        if not self.has_valid_moves(self.current_player):
            self.current_player = -self.current_player
            if not self.has_valid_moves(self.current_player):
                return True
        return False
