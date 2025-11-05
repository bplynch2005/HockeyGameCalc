from app import app
from flask import render_template, request, redirect, url_for, make_response
import requests
import re
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

from pyProgs.statParser.parse import parse
from pyProgs.statCalculator.calculate import calculate
from pyProgs.getGames.todaysGames import todaysGames, yesterdaysWinners
from pyProgs.gameLogger.logger import log, getYesterday

def getYesterdayGame():
    predictions = getYesterday()
    realWinners = yesterdaysWinners()
    count = 0

    for team in predictions:
        if team.strip() in realWinners:
            count += 1

    total = "I correctly predicted " + str(count) + " games out of " + str(len(predictions)) + " yesterday..."
    print(total)

def logData():
    schedule = todaysGames()
    statsList = []
    for matchup in schedule:
        teamStats = parse(matchup[0], matchup[1])
        statsList.append(teamStats)
    
    winnerList = []
    for stats in statsList:
        prediction = calculate(stats[0], stats[1], stats[2], stats[3])
        winnerList.append(prediction[0])

    log(winnerList)

scheduler = BackgroundScheduler()

if not scheduler.running:
    scheduler.add_job(getYesterdayGame, "interval", seconds=15)
    scheduler.add_job(logData, "interval", hours=24)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())

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
    finalData = {"teams": {"team1": {"name": teamStats[2], "stats": teamStats[0]}, "team2": {"name": teamStats[3], "stats": teamStats[1]}}, "prediction":{"betterTeam": prediction[0], "confidence": prediction[1], "decidingFactor": prediction[2]}}
    #*****Final steps. Creating cookies are returning*****
    resp = make_response(render_template("singleGame.html", data=finalData))
 
    return resp

@app.route('/todaysGames', methods=['GET', 'POST'])
def predict():
    schedule = todaysGames()
    statsList = []
    for matchup in schedule:
        teamStats = parse(matchup[0], matchup[1]) #teamStats[0] = team1Stats, teamStats[1] = team2Stats, teamStats[2] = team1_name, teamStats[3] = team2_name
        statsList.append(teamStats)
    
    winnerList = []
    for stats in statsList:
        prediction = calculate(stats[0], stats[1], stats[2], stats[3])
        finalData = {"teams": {"team1": {"name": stats[2], "stats": stats[0]}, "team2": {"name": stats[3], "stats": stats[1]}}, "prediction":{"betterTeam": prediction[0], "confidence": prediction[1], "decidingFactor": prediction[2]}}
        winnerList.append(finalData)

    resp = make_response(render_template("todaysGames.html", data=winnerList))
    return resp

@app.route('/index')
def index():
    return render_template('homePage.html')
