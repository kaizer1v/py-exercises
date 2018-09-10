from board import Board
from player import Player


class Game:
    def __init__(self, coins, players=2):
        # `move_names` is only for reference
        self.move_names = [
            'invalid',
            'strike',
            'multistrike',
            'red strike',
            'striker strike',
            'defunct coin',
            'none'
        ]
        self.move_sep = ','
        self.board = Board(coins)
        self.players = [Player() for i in range(players)]

    def get_board(self):
        return self.board.get_coins()

    def get_points(self):
        return list(map(Player.get_points, self.players))

    def is_finish(self):
        p_points = list(map(Player.get_points, self.players))
        return min(p_points) >= 5 and (
            abs(p_points[0] - p_points[1]) > 3
        ) or (self.board.get_coins()['black'] == 0)

    def get_winner(self):
        points = self.get_points()
        return points.index(max(points)) + 1

    def move(self, p, m):
        '''
        play the move <m> for the provided player <p>
        and update their player's points
        '''
        if m == 1:                            # strike
            self.players[p].add_points(1)
            self.board.remove_coins('black', 1)
        elif m == 2:                          # multi-strike
            self.players[p].add_points(2)
            self.board.remove_coins('black', 2)
        elif m == 3:                          # red-strike
            self.players[p].add_points(3)
            self.board.remove_coins('red', 1)
        elif m == 4:                          # striker-strike <foul>
            self.players[p].remove_points(1)
        elif m == 5:                          # defunct <foul>
            self.players[p].remove_points(2)
        elif m == 6:                          # none <miss>
            self.players[p].commit_miss()

    def play(self, moves):
        mvs = moves.split(self.move_sep)
        for p, m in enumerate(mvs):
            self.move(p, int(m))
