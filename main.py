import curses
import game

class MainWindow:

	def __init__(self, spielfeld):
		self.spielfeld = spielfeld
		self.width = 4
		self.inp = "nix gedrueckt"
	def __enter__(self):
		self.myscreen = curses.initscr()
		curses.curs_set(0)
		curses.start_color()

	def __exit__(self, type, value, traceback):
		curses.endwin()			

	def application(self):
		while 1:
			self.dims = self.myscreen.getmaxyx()
			self.myscreen.clear()
			dims = self.myscreen.getmaxyx()
			self.myscreen.border(0)
			# self.myscreen.addstr(dims[0]/2, dims[1]/2, "Hello World!", curses.A_BLINK)
			self.myscreen.addstr(1, 1, "2048", curses.A_BOLD)
			self.draw_field()
			self.myscreen.addstr(2, 1, str(self.inp), curses.A_NORMAL)			
			self.inp = self.myscreen.getch()
			self.myscreen.refresh()

	def draw_field(self):
		for i in xrange(5):
			self.myscreen.hline(self.dims[0]/2 +(i-2)*self.width, self.dims[1]/2-9, "-", 8*self.width-1)
		for i in xrange(5):	
			self.myscreen.vline(self.dims[0]/2 -2*self.width+1, self.dims[1]/2-10 +i*2*self.width, "|", 4*self.width)

		for i, number in enumerate(self.spielfeld.field.flat):
			if number != 0:
				self.draw_number(number, i)

		self.myscreen.addstr(self.dims[0]/2 -2*self.width-1, self.dims[1]/2-10, "Highscore:")


	def draw_number(self, number, index):
		pos = (self.dims[0]/2 + 2 + (index/4 - 2) * self.width, self.dims[1]/2-6 +(index %4) *2*self.width)
		self.myscreen.addstr(pos[0], pos[1], str(number))
