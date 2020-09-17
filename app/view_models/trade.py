

from app.view_models.book import BookViewModel

__author__ = '七月'


# GiftOrWish
class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self, single):
        """
        if single.create_datetime:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
         """
        return dict(
            user_name=single.user.nickname,
            id=single.id
        )


class MyTrades:
    def __init__(self, trades_of_mine, trade_count_list):
        self.trades = []

        self.__trades_of_mine = trades_of_mine
        self.__trade_count_list = trade_count_list

        self.trades = self.__parse()

    def __parse(self):
        temp_trades = []
        for trade in self.__trades_of_mine:
            my_trade = self.__matching(trade)
            temp_trades.append(my_trade)
        return temp_trades

    def __matching(self, trade):
        count = 0
        for trade_count in self.__trade_count_list:
            if trade.isbn == trade_count['isbn']:
                count = trade_count['count']
        r = {
            'wishes_count': count,
            'book': BookViewModel(trade.book),
            'id': trade.id
        }
        return r

















"""  
class MyTrades():
    def __init__(self, gifts_of_mine, wishes_count_list):
        self.trades = []
        self.trades = self._map()
        self.__gifts_of_mine = gifts_of_mine
        self.__wishes_count_list = wishes_count_list
    def _map(self):
        list = []

        for wish in self.__gifts_of_mine:
            r = {
                'wishes_count': 0,
                'book' : None

            }
            for trade in self.__wishes_count_list:
                if trade['isbn'] == wish.isbn:
                    r['wishes_count'] = trade['count']
            r['book'] = wish.book
            list.append(r)
        return list
        
"""

