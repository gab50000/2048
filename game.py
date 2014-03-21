#!/usr/python

import numpy as np

class Spielfeld:
	def __init__(self):
		self.field = np.zeros((4,4), int)

	def __repr__(self):
		r = "_________________________\n"

		for i in range(4):
			for j in range(4):
				

