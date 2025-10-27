from nhlTeams import NHLTeams

def calculate(team1Stats, team2Stats, team1_, team2_):
    #*****Calculating who has the better matchup based on the season stats*****
    team1 = NHLTeams[team1_]
    team2 = NHLTeams[team2_]
    team1Score = 0
    team2Score = 0
    boolWSTREAK = False
    decidingFactor = ""
    #We first want to compare who has better stats overall
    for key in team1Stats:
          if key == 'goalsAllowed' or key == 'SOGAllowed' or key == 'PIM':
               if team1Stats[key] > team2Stats[key]:
                    team2Score += 1
               elif team1Stats[key] < team2Stats[key]:
                    team1Score += 1
               continue

          if key == 'WSTREAK':
               if team1Stats[key][:1] == 'W' and team2Stats[key][:1] != 'W':
                    if (int(team1Stats[key][1:]) >= 3) or (int(team2Stats[key][1:]) >= 3):
                         team1Score += 3
                         boolWSTREAK = True
               if team1Stats[key][:1] == 'W' and team2Stats[key][:1] == 'W':
                    if (int(team1Stats[key][1:]) >= 3) and ((int(team1Stats[key][1:])) - (int(team2Stats[key][1:])) >= 2):
                         team1Score += 3
                         boolWSTREAK = True
               if team2Stats[key][:1] == 'W' and team1Stats[key][:1] != 'W':
                    if (int(team2Stats[key][1:]) >= 3) or (int(team1Stats[key][1:]) >= 3):
                         team2Score += 3
                         boolWSTREAK = True
               if team2Stats[key][:1] == 'W' and team1Stats[key][:1] == 'W':
                    if (int(team2Stats[key][1:]) >= 3) and ((int(team2Stats[key][1:])) - (int(team1Stats[key][1:])) >= 2):
                         team2Score += 3
                         boolWSTREAK = True
               continue

          if team1Stats[key] > team2Stats[key]:
               team1Score += 1
          elif team1Stats[key] < team2Stats[key]:
               team2Score += 1

    if team1Score < team2Score:
         betterTeam = team2
    elif team1Score > team2Score:
         betterTeam = team1
    else:
         betterTeam = "Evenly Matched!"

    sum = team1Score + team2Score
    guarentee = max((team1Score/sum),(team2Score/sum))
    

    if team1Score > team2Score:
          if ((team1Stats['goals'] <= team2Stats['goalsAllowed'])) and (team1Stats['SOG']+.5 >= team2Stats['SOGAllowed']):
              decidingFactor += " - Great Offensive Matchup - "
          if (((team1Stats['PP'] > 22) and (team2Stats['PK'] < 75)) and (team2Stats['PIM'] > team1Stats['PIM'])):
               decidingFactor += " - Decisive PowerPlay - "
    elif team2Score > team1Score:
          if ((team2Stats['goals'] <= team1Stats['goalsAllowed'])) and (team2Stats['SOG']+.5 >= team1Stats['SOGAllowed']):
               decidingFactor += " - Great Offensive Matchup - "
          if (((team2Stats['PP'] > 22) and (team1Stats['PK'] < 75)) and (team1Stats['PIM'] > team2Stats['PIM'])):
               decidingFactor += " - Decisive PowerPlay - "
    if boolWSTREAK:
         decidingFactor += ' - Team is Hot/Cold! - '
    if decidingFactor is "":
         decidingFactor = " - None--- Evenly Matched! - "

    finalized = [betterTeam, guarentee, decidingFactor]
    return finalized

