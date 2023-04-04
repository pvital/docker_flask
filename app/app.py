#
# app/server.py
# Copyright (c) 2020 Paulo Vital <paulo@vital.eng.br>
#

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!!!'