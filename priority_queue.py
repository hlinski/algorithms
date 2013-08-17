class PriorityQueue(object):
	"""docstring for PriorityQueue"""
	def __init__(self, array):
		self.array = array

	def less(self,i, j):
		if self.array[i] < self.array[j]:
			return True
		return False

	def exch(self, i, j):
		temp = self.array[i]
		self.array[i] = self.array[j]
		self.array[j] = temp

	def swim(self, k):
		while k > 1 and self.less(k/2, k):
			self.exch(k/2, k)
			k = k/2

	def sink():		
		pass

	def add(self, element):
		array.append(element)
		self.swim(len(array)-1)


array = [4,2,1]
queue = PriorityQueue(array)
queue.add(3)
print array
		