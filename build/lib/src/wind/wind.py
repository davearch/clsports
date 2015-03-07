# clsports
#
from curses import wrapper

class wind():
    def init(self):
        self.string = 'hello world!'

    def start(self, stdscr):
        stdscr.clear()
        stdscr.addstring(1, 1, self.string)
        stdscr.refresh()
        stdscr.getkey()

    def call(self, stdscr):
        wrapper(self.start)
