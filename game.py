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

		for i in range(4):
			r += "| "
			for j in range(4):
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

		ind = np.random.randint(len(freefields))

		if np.random.randint(2) == 0:
			self.field[ind/self.dims[1], ind % self.dims[1]] = 2
		else:
			self.field[ind/self.dims[1], ind % self.dims[1]] = 4


	def collapse(self, arr):
	#after rowmove make sure that the row begins with a number, move the next number closer and let it collapse if possible
		i = 0
		while i < len(arr)-1:
			j = i+1
			while arr[j] == 0 and j < len(arr)-1:
				j += 1
			if arr[i] == arr[j]:
				arr[i] += arr[j]
				arr[j] = 0
	#after collapse start anew with remaining array part
			else:
				if i+1 != j:
					arr[i+1] = arr[j]
					arr[j] = 0
			self.rowmove(arr[j:])


	def rowmove(self, arr):
	#remove all free fields at the beginning
		i = 0
		while arr[i] == 0:
			i += 1
		arr[:len(arr)-i] = arr[i:]
		arr[len(arr)-i:] = 0

	#collapse equal fields
		self.collapse(arr)





	def move(self, direction):
		if direction == "up":
			pass


def main(*args):
	pass 


