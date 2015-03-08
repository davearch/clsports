# sportsCommand
# 2015
#
# queries run through sportsdatallc.com NFL API
# HTTP GET requests return XML
from urllib2 import urlopen
from random import randint, randrange
import xml.etree.ElementTree as ET
from sportsCommand.nfl.team import team

class query():
    global tmp_dir
    tmp_dir = '/tmp/'

    def __init__(self):
        self.access_level = 't'  # trial
        self.version      = '1'
        self.api_key      = 'pvefrf2zntbzn73w9fhxhc4c'
        self.base_url     = 'https://api.sportsdatallc.org/'
        self.returnFormat = 'xml'
        self.league       = 'nfl-'

    def createBaseString(self):
        sstring = self.base_url + self.league + self.access_level + self.version
        return sstring

    def createString(self, misc):
        bstring = self.createBaseString()
        newString = bstring + misc + self.returnFormat + '?api_key=' + self.api_key
        return newString

    def getXML(self, string):
        #data = urlopen(string).read()
        try:
            tmp_file = tmp_dir + str(randint(0, randrange(1, 200)))
        except:
            raise
        response = urlopen(string)
        xml      = open(tmp_file, "w")
        xml.write(response.read())
        xml.close()
        sfile = open(tmp_file, "r")
        tree = ET.ElementTree()
        tree.parse(sfile)
        return tree

    def queryTeams(self):
        url = self.createString('/teams/hierarchy.')
        dataTree = self.getXML(url)
        #ET.dump(dataTree)
        root = dataTree.getroot()
        teams = []
        for item in root:
            for low in item:
                for b in low:
                    a = team(b.get('name'), b.get('market'), b.get('id'))
                    teams.append(a)
        return teams
