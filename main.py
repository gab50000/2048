import curses
import game
import math

curses_colors = [
    curses.COLOR_WHITE,
    curses.COLOR_CYAN,
    curses.COLOR_BLUE,
    curses.COLOR_GREEN,
    curses.COLOR_YELLOW,
    curses.COLOR_MAGENTA,
    curses.COLOR_RED,
    curses.COLOR_RED,
    curses.COLOR_RED,
    curses.COLOR_RED,
    curses.COLOR_RED,
]


class MainWindow:
    def __init__(self, spielfeld):
        self.spielfeld = spielfeld
        self.width = 4
        self.inp = "nix gedrueckt"
        self.gameover = False
        self.win = False

    def __enter__(self):
        self.myscreen = curses.initscr()
        curses.curs_set(0)
        curses.start_color()

        for i in range(1, 11):
            curses.init_pair(i, curses_colors[i], curses.COLOR_BLACK)

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
                self.draw("GAME OVER")
            elif self.win:
                self.draw("YOU WIN!")
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
            merged = [[] for i in range(4)]
            tempscore, factor = 0, 0
            if self.spielfeld.lines_movable(s, merged):
                while self.spielfeld.lines_movable(s, merged):
                    tempscore, factor = self.spielfeld.single_step(
                        s, merged, tempscore, factor
                    )
                    self.myscreen.clear()
                    self.draw_surroundings()
                    self.myscreen.refresh()
                    curses.napms(50)
                self.spielfeld.add_numbers()
                self.spielfeld.score += factor * tempscore
            if self.spielfeld.gameover(merged):
                self.gameover = True
            elif self.spielfeld.win():
                self.win = True

    def draw(self, text):
        self.myscreen.border(0)
        self.myscreen.addstr(4, self.dims[1] // 2, text, curses.A_BOLD)
        self.draw_field()
        curses.napms(50)

    def draw_surroundings(self):
        self.myscreen.border(0)
        self.myscreen.addstr(1, 1, "2048", curses.color_pair(1))  # curses.A_BOLD)
        self.draw_field()

    def draw_field(self):
        for i in range(5):
            self.myscreen.hline(
                self.dims[0] // 2 + (i - 2) * self.width,
                self.dims[1] // 2 - 9,
                "-",
                8 * self.width - 1,
            )
        for i in range(5):
            self.myscreen.vline(
                self.dims[0] // 2 - 2 * self.width + 1,
                self.dims[1] // 2 - 10 + i * 2 * self.width,
                "|",
                4 * self.width,
            )

        for i, number in enumerate(self.spielfeld.field.flat):
            if number != 0:
                self.draw_number(number, i)

        self.myscreen.addstr(
            self.dims[0] // 2 - 2 * self.width - 1,
            self.dims[1] // 2 - 10,
            "Score: " + str(self.spielfeld.score),
        )

    def draw_number(self, number, index):
        pos = (
            self.dims[0] // 2 + 2 + (index // 4 - 2) * self.width,
            self.dims[1] // 2 - 6 + (index % 4) * 2 * self.width,
        )
        self.myscreen.addstr(
            pos[0],
            pos[1],
            str(number),
            curses.color_pair(int(math.log(number, 2))) | curses.A_BOLD,
        )
