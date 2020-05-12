# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: pb2751
"""

#import statements
from flask import Flask, render_template
from crawler import medals_comparison
from recs import drink_pairing

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/1006")
def intro():
    return "1006 homepage"

# Rowing crawler
@app.route("/tracker")
def track():
    return medals_comparison() # put debug true here if you want to see print()

@app.route("/pairs")
def give_recs():
    return drink_pairing()

#start the server
if __name__ == "__main__":
    app.run()