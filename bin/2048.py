#!/usr/bin/python

import sys
sys.path.append("..")
import game
import main

g = game.Spielfeld()
mw = main.MainWindow(g)

with mw:
	mw.application()