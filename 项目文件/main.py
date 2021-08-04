import flask
from flask_cors import CORS
from flask import Flask
# from main_hw import app_hw

app = Flask(__name__)
# app.register_blueprint(app_hw)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app)

@app.route('/')
def index():
    return flask.send_from_directory('static', 'index.html')


@app.route('/three_d')
def three_d():
    return flask.send_from_directory('static', 'ngl-maeter/examples/webapp.html')

@app.route('/xiaoying')
def xiaoying():
    return flask.send_from_directory('static', 'cardcaptorsakura-gh-pages/index.html')

@app.route('/xitong')
def xitong():
    return flask.send_from_directory('static', 'xitong.html')

@app.route('/static/<fname>')
def sendfile(fname):
    return flask.send_from_directory('static', fname)

# https://icon-icons.com/icon/heart-love-like-favourite-follow/131237
# https://icon-icons.com/icon/heart-love-favorite-favourite/13187
@app.route('/favicon.ico') 
def favicon(): 
    return flask.send_from_directory('static', 'loveheart.ico', mimetype='image/vnd.microsoft.icon')

app.run(host='0.0.0.0', port=11666, debug=True)
