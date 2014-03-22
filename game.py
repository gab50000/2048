import numpy as np

class Spielfeld:
	def __init__(self, arr=None):
		if arr == None or arr != numpy.ndarray:
			self.field = np.zeros((4,4), int)
		else:
			if len(arr.shape) != 2:
				self.field = np.zeros((4,4), int)
			else:
				self.field = arr

		self.dims = self.field.shape

		self.add_numbers()
		self.add_numbers()


	def __repr__(self):
		r = "--------------\n"

		for i in xrange(4):
			r += "| "
			for j in xrange(4):
				if self.field[i,j] == 0:
					pass
				else:
					r+=str(self.field[i,j])
				r+=" | "
			r += "\n"
		r += "--------------\n"

		return r

	def add_numbers(self):
		freefields = []
		for i, field in enumerate(self.field.flat):
			if field == 0:
				freefields.append(i)

		ind = freefields[np.random.randint(len(freefields))]

		if np.random.randint(2) == 0:
			self.field[ind/self.dims[1], ind % self.dims[1]] = 2
		else:
			self.field[ind/self.dims[1], ind % self.dims[1]] = 4


	def line_movable(self, arr):
		for i, elem in enumerate(arr):
			if elem != 0 and i != 0 and (arr[i-1] == 0 or arr[i-1] == elem):
					return True
		return False

	def lines_movable(self, direction):
		if direction == "up":
			for i in xrange(self.field.shape[1]):
				if line_movable(self.field[:,i]):
					return True
			return False
		elif direction == "down":
			for i in xrange(self.field.shape[1]):
				if line_movable(self.field[::-1,i]):
					return True
			return False
		elif direction == "left":
			for i in xrange(self.field.shape[0]):
				if line_movable(self.field[i,:]):
					return True
			return False
		else:
			for i in xrange(self.field.shape[0]):
				if line_movable(self.field[i,::-1]):
					return True
			return False		

	def rowmove(self, arr):
		for i in xrange(arr.size-1):
			if arr[i] == 0 and arr[i+1] != 0:
				arr[i] = arr[i+1]
				arr[i+1] = 0
			elif arr[i] == arr[i+1]:
				arr[i] += arr[i+1]
				arr[i+1] = 0

	def move(self, direction):
		if direction == "up":
			for i in xrange(self.field.shape[1]):
				self.rowmove(self.field[:,i])
		elif direction == "down":
			for i in xrange(self.field.shape[1]):
				self.rowmove(self.field[::-1,i])
		elif direction == "left":
			for i in xrange(self.field.shape[0]):
				self.rowmove(self.field[i,:])
		else:
			for i in xrange(self.field.shape[0]):
				self.rowmove(self.field[i,::-1])


def main(*args):
	pass 


