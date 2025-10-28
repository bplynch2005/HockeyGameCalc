import requests
import re
from nhlTeams import NHLTeams

def parse(team1_, team2_):
    try:
        team1 = NHLTeams[team1_]
        team2 = NHLTeams[team2_]
    except Exception as e:
        return "invalid team entered"

    team1Stats = {'goals':None, 'SOG':None, 'PP':None, 'shooting':None, 'faceoff':None, 'goalsAllowed':None, 'SOGAllowed':None, 'PK':None, 'PIM':None, 'WSTREAK':None}
    team2Stats = team1Stats.copy()

    url = "https://www.thescore.com/nhl/teams/"
    pattern = r'>(\d+(?:\.\d+)?)<'
    patternStreak = r'([WL]\d+)'
    try:
        team1URL = url + team1 + '/stats'
        team2URL = url + team2 + '/stats'
    except Exception as e:
         return "invalid team entered"
    
    #*****This is where we parse the html for the data we need*****
    session = requests.Session()
    result = session.get(team1URL)
    returnedHTML = result.text
    lineParts = returnedHTML.split('<!-- -->)') #[0] is disregarded, [1] is goals, [2] is shots on goal, [3] is power play, [4] is shooting, [5] is faceoff, [6] is goals allowed, [7] is SOG allowed, [8] is penalty kill, [9] is penalty minutes
    
    match = re.search(pattern, lineParts[1])
    if match:
        team1Stats['goals'] = float(match.group(1))
    match = re.search(pattern, lineParts[2])
    if match:
        team1Stats['SOG'] = float(match.group(1))
    match = re.search(pattern, lineParts[3])
    if match:
         team1Stats['PP'] = float(match.group(1))
    match = re.search(pattern, lineParts[4])
    if match:
         team1Stats['shooting'] = float(match.group(1))
    match = re.search(pattern, lineParts[5])
    if match:
         team1Stats['faceoff'] = float(match.group(1))
    match = re.search(pattern, lineParts[6])
    if match:
        team1Stats['goalsAllowed'] = float(match.group(1))
    match = re.search(pattern, lineParts[7])
    if match:
         team1Stats['SOGAllowed'] = float(match.group(1))
    match = re.search(pattern, lineParts[8])
    if match:
         team1Stats['PK'] = float(match.group(1))
    match = re.search(pattern, lineParts[9])
    if match:
         team1Stats['PIM'] = float(match.group(1))
     

    lineParts = returnedHTML.split('</span></div><div class="TeamBanner__statCell--3nMmQ"><div class="TeamBanner__stat--2yaO9">') #0 is disregarded, 1 is the number we want
    match = re.search(patternStreak,lineParts[1])
    if match:
         team1Stats['WSTREAK'] = str(match.group(1))

#*******REPEAT THE ENTIRE PROCESS FOR TEAM2********

    session = requests.Session()
    result = session.get(team2URL)
    returnedHTML = result.text
    lineParts = returnedHTML.split('<!-- -->)') #[0] is disregarded, [1] is goals, [2] is shots on goal, [3] is power play, [4] is shooting, [5] is faceoff, [6] is goals allowed, [7] is SOG allowed, [8] is penalty kill, [9] is penalty minutes
    match = re.search(pattern, lineParts[1])
    if match:
        team2Stats['goals'] = float(match.group(1))
    match = re.search(pattern, lineParts[2])
    if match:
        team2Stats['SOG'] = float(match.group(1))
    match = re.search(pattern, lineParts[3])
    if match:
         team2Stats['PP'] = float(match.group(1))
    match = re.search(pattern, lineParts[4])
    if match:
         team2Stats['shooting'] = float(match.group(1))
    match = re.search(pattern, lineParts[5])
    if match:
         team2Stats['faceoff'] = float(match.group(1))
    match = re.search(pattern, lineParts[6])
    if match:
        team2Stats['goalsAllowed'] = float(match.group(1))
    match = re.search(pattern, lineParts[7])
    if match:
         team2Stats['SOGAllowed'] = float(match.group(1))
    match = re.search(pattern, lineParts[8])
    if match:
         team2Stats['PK'] = float(match.group(1))
    match = re.search(pattern, lineParts[9])
    if match:
         team2Stats['PIM'] = float(match.group(1))
    
    lineParts = returnedHTML.split('</span></div><div class="TeamBanner__statCell--3nMmQ"><div class="TeamBanner__stat--2yaO9">') #0 is disregarded, 1 is the number we want
    match = re.search(patternStreak,lineParts[1])
    if match:
         team2Stats['WSTREAK'] = str(match.group(1))

    teamStats = [team1Stats, team2Stats, team1_, team2_]
    return teamStats 
