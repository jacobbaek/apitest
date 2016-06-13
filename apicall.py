#!/usr/bin/python

"""
    it is very simple mirco web server for getting api result
"""

from flask import Flask, render_template, redirect, flash, make_response
from xml.etree import ElementTree as ET
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests

username = ''
password = ''
hostname = ''
base_url = "https://" + hostname
keystr = ''

app = Flask(__name__)

def get_PA_key():
    global keystr
    key_url = base_url + '/api/?type=keygen&user=' + username + '&password=' + password
    key_str = requests.get(key_url, verify=False)
    root = ET.fromstring(key_str.text)
    key = root.find('result').find('key')
    keystr = key.text

def get_interface_info():
    if_list = []
    req_url = base_url + '/api/?type=op&cmd=<show><interface>all</interface></show>&key=' + keystr
    data = requests.get(req_url, verify=False)
    print data.text
    root = ET.fromstring(data.text)
    ifs = root.find('result').find('hw')
    for names in ifs.iter('entry'):
        if_list.append(names.find('name').text)
    return if_list

def get_mgmt_info():
    return

#@app.route('/info.png')
#def info():
#    fig=Figure(None, figsize=(10,16), dpi=100)
#    ax=fig.add_subplot(111)
#    x =[]
#    y =[]

#    fig = plt.savefig('info.png', transparent=True, pad_inches=0)
#    return fig

@app.route('/')
def show_all():
    get_PA_key()
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    ifnames = get_interface_info()
    return render_template('index.html', interfaces=ifnames)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7777, debug=True)