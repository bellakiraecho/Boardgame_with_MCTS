import random
import math
import time
from game import Othello

class MCTSNode:
    def __init__(self, game, parent=None, move=None):
        self.game = game
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.wins = 0

    def is_fully_expanded(self):
        return len(self.children) == len(self.game.get_valid_moves(self.game.current_player))

    def best_child(self, exploration_weight=1.4):
        choices_weights = [
            (child.wins / child.visits) + exploration_weight * math.sqrt(2 * math.log(self.visits) / child.visits)
            for child in self.children
        ]
        return self.children[choices_weights.index(max(choices_weights))]

    def most_visited_child(self):
        if not self.children:
            return None
        return max(self.children, key=lambda c: c.visits)

    def expand(self):
        valid_moves = self.game.get_valid_moves(self.game.current_player)
        for move in valid_moves:
            if all(child.move != move for child in self.children):
                new_game = self.game.clone()
                new_game.make_move(move[0], move[1], new_game.current_player)
                child_node = MCTSNode(new_game, parent=self, move=move)
                self.children.append(child_node)
                return child_node
        return None

    def playout(self):
        current_game = self.game.clone()
        current_player = current_game.current_player

        while not current_game.is_game_over():
            possible_moves = current_game.get_valid_moves(current_player)
            if possible_moves:
                move = random.choice(possible_moves)
                current_game.make_move(move[0], move[1], current_player)
            current_player = -current_player
        
        winner = current_game.get_winner()
        if winner == self.game.current_player:
            return 1
        elif winner == -self.game.current_player:
            return -1
        else:
            return 0

    def backpropagate(self, result):
        self.visits += 1
        self.wins += result
        if self.parent:
            self.parent.backpropagate(-result)

class MCTS:
    def __init__(self, iterations=1000, time_limit=1.0):
        self.iterations = iterations
        self.time_limit = time_limit

    def select(self, node):
        while node.is_fully_expanded() and node.children:
            node = node.best_child()
        return node

    def expand(self, node):
        if not node.is_fully_expanded():
            return node.expand()
        return node

    def playout(self, node):
        return node.playout()

    def backpropagate(self, node, result):
        node.backpropagate(result)

    def get_best_move(self, game):
        root = MCTSNode(game)
        start_time = time.time()

        for _ in range(self.iterations):
            if self.time_limit > 0 and time.time() - start_time > self.time_limit:
                break

            node = self.select(root)
            if not node.is_fully_expanded():
                node = self.expand(node)
            result = self.playout(node)
            self.backpropagate(node, result)

        best_child = root.most_visited_child()
        if best_child:
            return best_child.move
        else:
            return random.choice(game.get_valid_moves(game.current_player))
