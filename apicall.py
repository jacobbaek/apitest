#!/usr/bin/python

"""
    it is very simple mirco web server for getting api result
"""

from flask import Flask, render_template, redirect, flash
import requests

# test call number
num = 1

app = Flask(__name__)

def call_api():
    url = 'http://movie.naver.com/movie/running/current.nhn'
    r = requests.get(url=url)
    return r.text

def call_test_api():
    global num
    num = num + 1
    return "value" + str(num)

@app.route('/')
def show_all():
    ret = call_test_api()
    ret2 = call_test_api()
    ret3 = call_api()
    return render_template('index.html', val1=ret, val2="value2", val3=ret2, val4=ret3)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7777, debug=True)