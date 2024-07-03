#!/usr/bin/env python3

'''Hello World!'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', method=['GET'], strict_slashes=False)
def hello_world() -> str:
    '''Hello World!'''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
