from datetime import date, timedelta

from nhlpy import NHLClient
from nhlTeams import NHLTeams_Abbrev

def todaysGames():
    client = NHLClient()
    games = client.schedule.daily_schedule()
    retList = []
    for game in games.get('games', []):
        away_team = game['awayTeam']['abbrev'].upper()
        home_team = game['homeTeam']['abbrev'].upper()

        currGame = (NHLTeams_Abbrev.inv[away_team], NHLTeams_Abbrev.inv[home_team])
        retList.append(currGame)

    return retList

def yesterdaysWinners():
    client = NHLClient()
    scores = client.game_center.daily_scores(date=str(date.today()-timedelta(days=1)))
    winnerList = []

    for game in scores["games"]:
        home = NHLTeams_Abbrev.inv[game["homeTeam"]["abbrev"].upper()]
        away = NHLTeams_Abbrev.inv[game["awayTeam"]["abbrev"].upper()]
        home_score = game["homeTeam"]["score"]
        away_score = game["awayTeam"]["score"]

        if home_score > away_score:
            winner = home
        elif away_score > home_score:
            winner = away
        else:
            winner = "Tie"

        winnerList.append(winner)

    return winnerList
