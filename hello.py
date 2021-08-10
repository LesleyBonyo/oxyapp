# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:29:23 2021

@author: Lesley
"""


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'