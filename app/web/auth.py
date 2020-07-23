
from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user

from app.forms.auth import RegisterForm, LoginForm
from app.models.base import db
from app.models.user import User
from . import web

__author__ = '七月'

@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    '''
    1检验数据是否合法
    2检验数据邮箱这个用户是否存在，存在的话，密码是否对得上，这个都可以用第三方Form来验证
    3写入cookie,到对方，对方上次把Id带来，和session中的一对，发现数据库中如果有的话，就给对方返回登录后才会显示的页面，比如首面右上角的"注销',
    4重构login,它除了能返回主页，还能返回到之前的跳转的页面
    :return:
    '''
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            if request.args:
                next = request.args['next']
                redirect(next)
            return render_template('index.html')
        else:
            flash('账号不存在或密码错误')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
