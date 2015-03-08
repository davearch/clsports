# sportsCommand
# 2015
#
import xml.etree.ElementTree as ET
class team():
    league_id = 'NFL'

    def __init__(self, name):
        self.name       = name
        self.team_id    = ''
        self.roster     = []
        self.coaches    = []
        self.owner      = ''
        self.record     = []
        self.division_id   = ''
        self.conference_id = ''
