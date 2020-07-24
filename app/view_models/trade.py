class Trade():
    def __init__(self, wish):
        self.user_name = wish.user.user_name
        self.time = wish.create_time
        self.id = wish.id

class Wishesinfo():
    def __init__(self,data):
        self.total = 0
        self.trades = []
        self._convert(data)

    def _convert(self, data):
        self.total = len(data)
        self.trades = [Trade(x) for x in data]
