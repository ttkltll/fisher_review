from flask import Flask, current_app, request, Request

app = Flask(__name__)
ctx = app.app_context()
ctx.push()
current_app.static_floder = 'static'
ctx.pop()
app.run

