# sportsCommand
# 2015

from sportsCommand.query.query import query

class leagueNFL(league):
    name        = 'NFL'
    league_id   = 'NFL'
    conferences = ['AFC', 'NFC']
    divisions   = ['AFC_EAST', 'AFC_NORTH', 'AFC_WEST', 'AFC_SOUTH'
                   'NFC_EAST', 'NFC_NORTH', 'NFC_WEST', 'NFC_SOUTH']
    teams       = []

    def __init__(self):
        self.test = 'test'
