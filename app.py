# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: pb2751
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/1006")
def intro():
    return "1006 homepage"

# COVID crawler
@app.route("/tracker")
def track():
    return "COVID-19 with Pandas"

@app.route("/songs")
def give_recs():
    return "Interact with Spotify RESTful API"

#start the server
if __name__ == "__main__":
    app.run()