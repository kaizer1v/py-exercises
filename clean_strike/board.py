class Board:
    '''
    creates a board with the specified coin settings
    '''
    def __init__(self, coins):
        self.coins = coins

    def add_coins(self, ct, q):
        '''
        add coin(s) based on the coin type `ct`
        provided and return board setting
        '''
        self.coins[ct] += q
        return self.coins

    def remove_coins(self, ct, q=1):
        '''
        remove coin(s) based on the coin type `ct`
        by the quantity provided `q`
        '''
        if not self.coins[ct] == 0:
            self.coins[ct] -= q
        return self.coins

    def get_coins(self):
        return self.coins
