import random
import math
import time

class MCTSNode:
    def __init__(self, state, parent=None, parent_action=None):
        self.state = state
        self.parent = parent
        self.parent_action = parent_action
        self.children = []
        self.visits = 0
        self.wins = 0

    def is_fully_expanded(self):
        return len(self.children) == len(self.state.get_empty_squares())

    def best_child(self, c_param=1.4):
        choices_weights = [
            (child.wins / child.visits) + c_param * math.sqrt((2 * math.log(self.visits) / child.visits))
            for child in self.children
        ]
        return self.children[choices_weights.index(max(choices_weights))]

    def best_action(self):
        visits = [child.visits for child in self.children]
        return self.children[visits.index(max(visits))].parent_action

class MCTS:
    def __init__(self, game, time_limit=1.0):
        self.game = game
        self.time_limit = time_limit

    def run(self):
        root = MCTSNode(state=self.game.copy())
        end_time = time.time() + self.time_limit

        while time.time() < end_time:
            node = self.select(root)
            if not node.state.is_game_over():
                node = self.expand(node)
            result = self.playout(node.state.copy())
            self.backpropagate(node, result)

        return root.best_action()

    def select(self, node):
        while node.is_fully_expanded() and not node.state.is_game_over():
            node = node.best_child()
            node.state = node.state.copy()
            node.state.make_move(*node.parent_action)
        return node

    def expand(self, node):
        action = self.prioritize_actions(node.state)
        if action is None:
            action = random.choice(node.state.get_empty_squares())
        new_state = node.state.copy()
        new_state.make_move(*action)
        child_node = MCTSNode(state=new_state, parent=node, parent_action=action)
        node.children.append(child_node)
        return child_node

    def playout(self, state):
        current_simulation_state = state
        while not current_simulation_state.is_game_over():
            possible_moves = current_simulation_state.get_empty_squares()
            move = random.choice(possible_moves)
            current_simulation_state.make_move(*move)
        if current_simulation_state.current_winner == self.game.current_player:
            return 1
        elif current_simulation_state.current_winner is None:
            return 0.5
        else:
            return 0

    def backpropagate(self, node, result):
        while node is not None:
            node.visits += 1
            node.wins += result
            node = node.parent

    def prioritize_actions(self, state):
        empty_squares = state.get_empty_squares()
        current_player = state.current_player
        opponent = 'O' if current_player == 'X' else 'X'

        # Check for winning move
        for move in empty_squares:
            state_copy = state.copy()
            state_copy.make_move(*move)
            if state_copy.current_winner == current_player:
                return move

        # Check for blocking opponent's winning move
        for move in empty_squares:
            state_copy = state.copy()
            state_copy.current_player = opponent
            state_copy.make_move(*move)
            if state_copy.current_winner == opponent:
                return move

        # Add heuristic: try to create a fork or block opponent's fork
        for move in empty_squares:
            state_copy = state.copy()
            state_copy.make_move(*move)
            if self.creates_fork(state_copy, current_player):
                return move

        for move in empty_squares:
            state_copy = state.copy()
            state_copy.make_move(*move)
            if self.creates_fork(state_copy, opponent):
                return move

        return None

    def creates_fork(self, state, player):
        winning_moves = 0
        empty_squares = state.get_empty_squares()
        for move in empty_squares:
            state_copy = state.copy()
            state_copy.make_move(*move)
            if state_copy.current_winner == player:
                winning_moves += 1
        return winning_moves > 1
