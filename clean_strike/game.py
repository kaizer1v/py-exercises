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

    def __print_name__(self, p, m):
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
        empty_board = board['black'] == 0 and board['red'] == 0
        points_crossed = min(points) >= 5 and (abs(points[0] - points[1]) > 3)
        return empty_board or points_crossed

    def get_result(self):
        points = self.get_points()
        board = self.get_board()
        min_p = min(points)
        max_p = max(points)
        if min_p >= 5 and (abs(points[0] - points[1]) > 3):
            return points.index(max_p) + 1 # returns winner player number
        elif (min_p <= 5 and max_p <= 5) or (min_p == max_p):
            return 'draw'                  # draw

    def get_winner(self):
        points = self.get_points()
        return points.index(max(points)) + 1

    def move(self, p, m):
        '''
        play the move for the provided player
        and update their player's points
        '''        
        if m == 1:                            # strike
            if self.board.get_coins()['black'] >= 1:
                self.players[p].add_points(1)
                self.board.remove_coins('black', 1)
        elif m == 2:                          # multi-strike
            if self.board.get_coins()['black'] >= 2:
                self.players[p].add_points(2)
                self.board.remove_coins('black', 2)
        elif m == 3:                          # red-strike
            if self.board.get_coins()['red'] != 0:
                self.players[p].add_points(3)
                self.board.remove_coins('red', 1)
        elif m == 4:                          # striker-strike <foul>
            self.players[p].remove_points(1)
        elif m == 5:                          # defunct <foul>
            self.players[p].remove_points(2)
        elif m == 6:                          # none <miss>
            self.players[p].commit_miss()
        self.__print_name__(p, m)

    def play(self, moves):
        mvs = moves.split(self.move_sep)
        for p, m in enumerate(mvs):
            self.move(p, int(m))
