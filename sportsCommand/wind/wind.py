# clsports
#
from curses import wrapper

class wind():
    def __init__(self):
        self.string = 'hello world!'

    def start(self, stdscr):
        stdscr.clear()
        stdscr.border()
        stdscr.addstr(1, 1, self.string)
        stdscr.refresh()
        stdscr.getkey()

    def call(self):
        wrapper(self.start)
