from flask import Flask
import time
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page\n'


@app.route('/one')
def one():
    time.sleep(1)
    return 'one\n'


@app.route('/ten')
def ten():
    time.sleep(10)
    return 'ten\n'


@app.route('/thirty')
def thirty():
    time.sleep(30)
    return 'ten\n'


@app.route('/minute')
def minute():
    time.sleep(60)
    return 'ten\n'


if __name__ == '__main__':
    app.run()


