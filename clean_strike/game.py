from board import Board
from player import Player


class Game:

    def __init__(self, coins, players=2):
        self.board = Board(coins)
        self.players = [Player() for i in range(players)]

    def show_board(self):
        return self.board.get_coins()

    def show_points(self):
        return list(map(Player.get_points, self.players))

    def can_have_winner(self):
        '''checks eligibility for having a definite winner'''
        p_points = list(map(Player.get_points, self.players))
        return min(p_points) >= 5 and (abs(p_points[0] - p_points[1]) > 3)

    def play(self, p, opt):
        '''
        given an option, play game with that option
        and update the points
        '''
        if opt == 1:                # strike
            self.players[p].add_points(1)
            self.board.remove_coins('black', 1)
        elif opt == 2:              # multi-strike
            self.players[p].add_points(2)
            self.board.remove_coins('black', 2)
        elif opt == 3:              # red-strike
            self.players[p].add_points(3)
            self.board.remove_coins('red', 1)
        elif opt == 4:              # striker-strike
            self.players[p].remove_points(1)
        elif opt == 5:              # defunct         
            self.players[p].remove_points(2)
        elif opt == 6:
            self.players[p].commit_foul()
