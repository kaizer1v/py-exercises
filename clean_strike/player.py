class Player:
    '''creates a player and logs their points and fouls'''
    def __init__(self):
        self.points = 0
        # self.misses = 0
        self.fouls = 0
        # self.is_foul = False

    def add_points(self, p=1):
        self.points += p
        return self.points

    def remove_points(self, p=1):
        self.commit_foul()
        self.points -= p
        return self.points

    def commit_miss(self):
        if self.misses = 3:
            self.remove_points(1)
            self.misses = 0
        else:
            self.misses += 1

    def commit_foul(self):
        if self.fouls % 3 == 0:
            self.remove_points(1)
        else:
            self.fouls += 1

    def get_points(self):
        return self.points
