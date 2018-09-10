class Player:
    '''creates a player and logs their points and fouls'''
    def __init__(self):
        self.points = 0
        self.is_foul = False
        self.foul_count = 0

    def add_points(self, p=1):
        self.points += p
        return self.points

    def remove_points(self, p=1):
        self.points -= p
        return self.points

    def commit_foul(self):
        if not self.is_foul:
            self.is_foul = True
        self.foul_count += 1
        return self.foul_count

    def get_points(self):
        return self.points
