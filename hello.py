# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 12:32:20 2019

@author: 140524
"""

from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)
app.add_url_rule('/','hello',hello_world)    
    
