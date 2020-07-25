

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
        if single.create_datetime:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )

class MyTrades():
    def __init__(self, lists_mine, count_list):
        self.trades = []
        self._map(lists_mine, count_list )

    def _map(self, lists_mine, count_list ):
        self.trades = [for x in lists_mine]
        # 写到这，我不知道怎么写，这里看似要用两个列表推导式组合成一个。


