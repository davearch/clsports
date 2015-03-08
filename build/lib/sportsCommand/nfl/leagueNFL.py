# sportsCommand
# 2015

from sportsCommand.query.query import query
from sportsCommand.nfl.team import team

class leagueNFL():
    name        = 'NFL'
    league_id   = 'NFL'
    conferences = ['AFC', 'NFC']
    divisions   = ['AFC_EAST', 'AFC_NORTH', 'AFC_WEST', 'AFC_SOUTH'
                   'NFC_EAST', 'NFC_NORTH', 'NFC_WEST', 'NFC_SOUTH']
    teams       = ['Tampa Bay Buccaneers',
                   'Tennessee Titans',
                   'Jacksonville Jaguars',
                   'Oakland Raiders',
                   'Washington Redskins',
                   'New York Jets',
                   'Chicago Bears',
                   'Atlanta Falcons',
                   'New York Giants',
                   'St. Louis Rams',
                   'Minnesota Vikings',
                   'Cleveland Browns',
                   'New Orleans Saints',
                   'New Orleans Saints',
                   'San Francisco 49ers',
                   'Houston Texans',
                   'San Diego Chargers',
                   'Kansas City Chiefs',
                   'Cleveland Browns',
                   'Philadelphia Eagles',
                   'Cincinnati Bengals',
                   'Pittsburgh Steelers',
                   'Detroit Lions',
                   'Arizona Cardinals',
                   'Carolina Panthers',
                   'Baltimore Ravens',
                   'Dallas Cowboys',
                   'Denver Broncos',
                   'Indianapolis Colts',
                   'Green Bay Packers',
                   'Seattle Seahawks',
                   'New England Patriots',
                   'Buffalo Bills']

    def __init__(self):
        for item in self.teams:
            a = team(item)
