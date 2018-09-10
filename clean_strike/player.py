class Player:
    '''creates a player and logs their points and fouls'''
    def __init__(self):
        self.points = 0
        self.fouls = 0
        self.misses = 0
        self.is_miss = False

    def add_points(self, p=1):
        self.points += p
        self.__reset_miss__()
        return self.points

    def remove_points(self, p=1):
        self.points -= p
        self.__reset_miss__()
        self.__commit_foul__()
        return self.points

    def get_points(self):
        return self.points

    def commit_miss(self):
        self.misses += 1
        self.is_miss = True
        if self.misses == 3:
            self.points -= 1
            self.__reset_miss__()

    def __reset_miss__(self):
        self.misses = 0
        self.is_miss = False

    def __commit_foul__(self):
        '''
        a player loses a point every 3rd foul
        even if not successive
        '''
        self.fouls += 1
        if self.fouls % 3 == 0:
            self.points -= 1
        return self.points
