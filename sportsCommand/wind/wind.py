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
    elif input == KEY_UP:
        print("up")
    elif input == KEY_DOWN:
        print("down")
    elif input == 13:
        print("Success")

class wind():
    def __init__(self, pane):
        self.pane = pane
        self.string = 'sportsCommand'

    def go(self, stdscr):
        stdscr.border()
        for team in self.pane.teams:
            stdscr.addstr(team + "\n")
        stdscr.refresh()

    def gostart(self):
        wrapper(self.go)

    def start(self, stdscr):
        stdscr.clear()
        stdscr.border()
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
