import curses
import game

class MainWindow:

	def __init__(self, spielfeld):
		self.spielfeld = spielfeld

	def __enter__(self):
		self.myscreen = curses.initscr()

	def __exit__(self, type, value, traceback):
		curses.endwin()			

	def application(self):
		while 1:
			self.myscreen.clear()
			dims = self.myscreen.getmaxyx()
			self.myscreen.border(0)
			# self.myscreen.addstr(dims[0]/2, dims[1]/2, "Hello World!", curses.A_BLINK)
			self.myscreen.addstr(1, 1, "2048", curses.A_BOLD)
			draw_field(self.myscreen, self.spielfeld)
			self.myscreen.getch()
			self.myscreen.refresh()

def draw_field(screen, spielfeld):
	width = 4
	dims = screen.getmaxyx()
	for i in xrange(5):
		screen.hline(dims[0]/2 +(i-2)*width, dims[1]/2-9, "-", 8*width-1)
	for i in xrange(5):	
		screen.vline(dims[0]/2 -2*width+1, dims[1]/2-10 +i*2*width, "|", 4*width)
	screen.addstr(dims[0]/2 -2*width-1, dims[1]/2-10, "Highscore:")

	# def draw_number(self, screen, number, index):
	# 	screen.addstr
