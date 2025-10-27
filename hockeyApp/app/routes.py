from app import app
from flask import render_template, request, redirect, url_for, make_response
import requests
import re

from pyProgs.statParser.parse import parse
from pyProgs.statCalculator.calculate import calculate

@app.route('/')
def method():
    return render_template('homePage.html')


@app.route('/seasonStats', methods=['GET', 'POST'])
#this is where we show the season stats for both teams
def getData(): 
    try:
        teamStats = parse(request.form['team1'].upper(), request.form['team2'].upper())
    except Exception as e:
        return render_template('homePage.html') #team does not exist
    prediction = calculate(teamStats[0], teamStats[1], teamStats[2], teamStats[3])

    #*****Creating HTML for the webpage we wish to show***** 
    finalData = {"teams": {"team1": {"name": teamStats[2], "stats": teamStats[0]}, "team2": {"name": teamStats[3], "stats": teamStats[1]}}, "prediction": {"betterTeam": prediction[0], "confidence": prediction[1], "decidingFactor": prediction[2]}}
    #*****Final steps. Creating cookies are returning*****
    resp = make_response(render_template("singleGame.html", data=finalData))
 
    return resp

@app.route('/predictions', methods=['GET', 'POST'])
def predict():
    return render_template('homePage.html')
    

@app.route('/index')
def index():
    return render_template('homePage.html')
