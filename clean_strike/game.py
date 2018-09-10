from board import Board
from player import Player


class Game:

    def __init__(self, coins, players=2):
        self.move_sep = ','
        self.board = Board(coins)
        self.players = [Player() for i in range(players)]

    def get_board(self):
        return self.board.get_coins()

    def get_points(self):
        return list(map(Player.get_points, self.players))

    def is_finish(self):
        '''checks eligibility for having a finished game'''
        p_points = list(map(Player.get_points, self.players))
        return min(p_points) >= 5 and (
            abs(p_points[0] - p_points[1]) > 3
        ) or (self.board.get_coins()['black'] == 0)

    def get_winner(self):
        points = self.get_points()
        return points.index(max(points)) + 1

    def play_single(self, p, opt):
        '''
        given an option, play game with that option
        and update the points
        '''
        if opt == 1:                            # strike
            self.players[p].add_points(1)
            self.board.remove_coins('black', 1)
        elif opt == 2:                          # multi-strike
            self.players[p].add_points(2)
            self.board.remove_coins('black', 2)
        elif opt == 3:                          # red-strike
            self.players[p].add_points(3)
            self.board.remove_coins('red', 1)
        elif opt == 4:                          # striker-strike
            self.players[p].remove_points(1)
        elif opt == 5:                          # defunct         
            self.players[p].remove_points(2)
        elif opt == 6:
            self.players[p].commit_foul()

    def play(self, moves):
        mvs = moves.split(self.move_sep)
        for p, m in enumerate(mvs):
            self.play_single(p, int(m))
