import curses
import game

class MainWindow:

	def __init__(self, spielfeld):
		self.spielfeld = spielfeld
		self.width = 4
		self.inp = "nix gedrueckt"
		self.gameover = False
	def __enter__(self):
		self.myscreen = curses.initscr()
		curses.curs_set(0)
		curses.start_color()

	def __exit__(self, type, value, traceback):
		curses.endwin()			

	def application(self):
		while 1:
			self.myscreen.clear()
			self.check_input()
			self.dims = self.myscreen.getmaxyx()
			dims = self.myscreen.getmaxyx()
			self.draw_surroundings()
			if self.gameover:
				self.draw_gameover()
			else:
				self.inp = self.myscreen.getch()
			self.myscreen.refresh()

	def check_input(self):
		if self.inp == 65:
			s = "up"
		elif self.inp == 66:
			s = "down"
		elif self.inp == 68:
			s = "left"
		elif self.inp == 67:
			s = "right"
		else:
			s = "?"

		if s != "?":
			merged = [[] for i in xrange(4)]
			tempscore, factor = 0, 0
			if self.spielfeld.lines_movable(s, merged):
				while self.spielfeld.lines_movable(s, merged):
					tempscore, factor = self.spielfeld.single_step(s, merged, tempscore, factor)
					self.myscreen.clear()
					self.draw_surroundings()
					self.myscreen.addstr(5, 1, " ".join([" ".join(map(str, m)) for m in merged]), curses.A_BOLD)
					self.myscreen.refresh()
					curses.napms(50)
				self.spielfeld.add_numbers()
				self.spielfeld.score += factor * tempscore
			if self.spielfeld.gameover(merged):
				self.gameover = True

	def draw_gameover(self):
		self.myscreen.border(0)
		self.myscreen.addstr(1, 1, "2048", curses.A_BOLD)
		self.myscreen.addstr(4, self.dims[1]/2, "GAME OVER", curses.A_BOLD)
		self.draw_field()			
		curses.napms(50)
				

	def draw_surroundings(self):
		self.myscreen.border(0)
		self.myscreen.addstr(1, 1, "2048", curses.A_BOLD)
		self.draw_field()			

	def draw_field(self):
		for i in xrange(5):
			self.myscreen.hline(self.dims[0]/2 +(i-2)*self.width, self.dims[1]/2-9, "-", 8*self.width-1)
		for i in xrange(5):	
			self.myscreen.vline(self.dims[0]/2 -2*self.width+1, self.dims[1]/2-10 +i*2*self.width, "|", 4*self.width)

		for i, number in enumerate(self.spielfeld.field.flat):
			if number != 0:
				self.draw_number(number, i)

		self.myscreen.addstr(self.dims[0]/2 -2*self.width-1, self.dims[1]/2-10, "Score: "+str(self.spielfeld.score))


	def draw_number(self, number, index):
		pos = (self.dims[0]/2 + 2 + (index/4 - 2) * self.width, self.dims[1]/2-6 +(index %4) *2*self.width)
		self.myscreen.addstr(pos[0], pos[1], str(number))
