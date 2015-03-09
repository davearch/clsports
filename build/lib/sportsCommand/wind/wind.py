# clsports
#
import curses
from curses import wrapper
import curses.textpad
from curses.textpad import Textbox
from sportsCommand.nfl.leagueNFL import leagueNFL
from sportsCommand.nfl.team import team
from sportsCommand.query.query import query


def valid(input):
    league = leagueNFL()
    newin  = wind(league)
    if input == 9:
        newin.gostart()
    elif input == 10:
	newin.callPlayers()
    else:
	print(input)

class wind():
    def __init__(self, pane):
        self.pane = pane
	self.players = ['Antonio Brown',
			'Tom Brady',
			'Marshawn Lynch']
        self.string = 'sportsCommand'


    def callPlayers(self):
	wrapper(self.listPlayers)

    def listPlayers(self, stdscr):
	stdscr.clear()
	stdscr.border()
	stdscr.addstr(1, 20, "select by player")
	for counter, player in enumerate(self.players, start=2):
	    stdscr.addstr(counter, 2, player)
	stdscr.refresh()
        box = Textbox(stdscr)
        box.edit(valid)

    def go(self, stdscr):
	stdscr.clear()
        stdscr.border()
	stdscr.addstr(1, 20, "select by team")
	for counter, team in enumerate(self.pane.teams, start=2):
	    left = 2
	    if counter > 18:
		left = 40
		stdscr.addstr(counter - 17, left, team)
	    else:
		stdscr.addstr(counter, left, team)
        stdscr.refresh()
        box = Textbox(stdscr)
        box.edit(valid)

    def gostart(self):
        wrapper(self.go)

    def start(self, stdscr):
        stdscr.clear()
        stdscr.border()
	stdscr.addstr(20, 20, self.string)
	stdscr.addstr(21, 20, "(Press Tab to view teams)")
	stdscr.addstr(22, 20, "(Press Enter to view players)")
        box = Textbox(stdscr)
        stdscr.refresh()
        box.edit(valid)
        stdscr.refresh()
        stdscr.getkey()

    def call(self):
        wrapper(self.start)

    def printTeams(self):
        begin_x = 20
        begin_y = 7
        height  = 5
        width   = 40
        win = curses.newwin(height, width, begin_y, begin_x)
        for team in self.pane.teams:
            print(team + "\n")
