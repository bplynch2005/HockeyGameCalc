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

