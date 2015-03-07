# sportsCommand
# 2015
#
# queries run through sportsdatallc.com NFL API
# HTTP GET requests return XML

import urllib2
import xml.etree.ElementTree as ET

class query():
    def __init__(self):
        access_level = 't'  # trial
        version      = 'v1'
        api_key      = 'pvefrf2zntbzn73w9fhxhc4c'
        base_url     = 'https://api.sportsdatallc.org/'
        returnFormat = 'xml'

    def createString(self):
