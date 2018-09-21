import collections
from board import Board
from player import Player


class Game:
    def __init__(self, coins, players=2):
        # `move_names` is only for reference
        self.move_names = [
            'strike',
            'multistrike',
            'red strike',
            'striker strike',
            'defunct coin',
            'none'
        ]
        self.points = {     # points based on color
            'white': 2,
            'black': 1,
            'red': 2
        }
        self.move_sep = ','
        self.board = Board(coins)
        self.players = [Player() for i in range(players)]

    def __print_details__(self, p, m):
        print('Player{} played {}. Score is {}. {}'.format(
            p,
            self.move_names[m],
            self.get_points(),
            self.get_board()
        ))

    def get_board(self):
        return self.board.get_coins()

    def get_points(self):
        return list(map(Player.get_points, self.players))

    def is_game_over(self):
        board = self.get_board()
        points = self.get_points()
        empty_board = board['black'] == 0 and board['red'] == 0 and board['white'] == 0
        points_crossed = min(points) >= 5 and (abs(points[0] - points[1]) > 3)
        return empty_board or points_crossed

    def get_result(self):
        points = self.get_points()
        board = self.get_board()
        min_p = min(points)
        max_p = max(points)
        if max_p >= 5 and (abs(points[0] - points[1]) > 3):
            return points.index(max_p) + 1  # returns winner player number
        elif (min_p <= 5 or max_p <= 5) or (min_p == max_p):
            return 'draw'                   # draw

    def get_winner(self):
        points = self.get_points()
        return points.index(max(points)) + 1

    def strike(self, p, c):
        if not self.board.get_coins()[c[0]] <= 0:
            self.players[p].add_points(self.points[c[0]])
            self.board.remove_coins(c[0], 1)

    def multistrike(self, p, c):
        counts = collections.Counter(c)
        for ct, q in counts.items():
            if not self.board.get_coins()[ct] <= 0:
                self.players[p].add_points(q * self.points[ct])
                self.board.remove_coins(ct, q)

    def red_strike(self, p, c):
        if c[0] == 'red' and self.board.get_coins()[c[0]] != 0:
            self.players[p].add_points(3)
            self.board.remove_coins(c[0], 1)

    def striker_strike(self, p, c):
        self.players[p].remove_points(1)

    def defunct(self, p, c):
        self.players[p].remove_points(2)

    def nothing(self, p, c):
        self.players[p].commit_miss()

    def move(self, p, m, coins):
        '''
        play the move <m> for the provided player
        and update player's <p> points
        '''
        funcs = [
            self.strike,
            self.multistrike,
            self.red_strike,
            self.defunct,
            self.striker_strike,
            self.nothing
        ]
        funcs[m](p, coins)

    def play(self, moves):
        mvs = moves.split(self.move_sep)
        print('Player {}, played {}, {}, with {}'.format(
            int(mvs[0]),
            int(mvs[1]),
            self.move_names[int(mvs[1])],
            mvs[2:]
        ))
        if not self.is_game_over():
            self.move(int(mvs[0]), int(mvs[1]), mvs[2:])
            print('now points {}'.format(self.get_points()))
