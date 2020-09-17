
from flask import session, make_response, json, request, current_app, flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from app.models.base import db
from app.models.gift import Gift
from app.view_models.book import BookViewModel
from app.view_models.trade import MyTrades
from . import web




@web.route('/my/gifts')
@login_required
def my_gifts():
    """
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid) # 拿到当前用户的所有gift对象列表
    isbn_list = [gift.isbn for gift in gifts_of_mine] # 得到一个列表，这个列表是用户的gift对象的isbn列表
    wish_count_list = Gift.get_wish_counts(isbn_list) # 得到一个列表，这个列表里面是字典，字典有两个键值对,一个count,一个isbn
    # 拿到了这个用户的礼物对象列表。还有每个礼物的isbn和对应有多少个礼物。对接的数据：一个gifts列表，列表里是对象gift,它有属性book(BookViewModel),wishes_count,id
    view_model = MyTrade(gifts_of_mine, isbn_list)
    return render_template('my_gifts.html', gifts=view_model)
    """

    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid) # 拿到这个uid的所有gift列表
    isbn_list = [gift.isbn for gift in gifts_of_mine] # 把这个列表转换成一个由isbn组成的列表
    wish_count_list = Gift.get_wish_counts(isbn_list) # 通过一个数组参数，拿到一个列表，这个列表只有每个isbn对应的想要人数。[(count,isbn), (count, isbn)],这里只做一次查询。一个列表进去，然后出来一个列表。
    view_model = MyTrades(gifts_of_mine, wish_count_list)
    return render_template('my_gifts.html', gifts=view_model.trades)

@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        # 事务
        # rollback
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass

