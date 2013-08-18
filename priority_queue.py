class PriorityQueue(object):
    """docstring for PriorityQueue"""

    def __init__(self, array):
        self.array = array

    def less(self, i, j):
        if self.array[i] < self.array[j]:
            return True
        return False

    def exch(self, i, j):
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def swim(self, k):
        while k > 1 and self.less(k / 2, k):
            self.exch(k / 2, k)
            k = k / 2

    def sink(self, k):
        while 2 * k <= len(self.array):
            j = 2 * k
            if j < len(self.array)-1:
                if self.less(j, j + 1):
                    j = j + 1
            if not self.less(k, j):
                break
            self.exch(k, j)
            k = j

    def add(self, element):
        array.append(element)
        self.swim(len(array) - 1)

    def take(self):
        max = self.array[1]
        self.exch(1, len(self.array) - 1)
        del self.array[len(self.array) - 1]
        self.sink(1)
        return max


array = [-1]
queue = PriorityQueue(array)
queue.add(2)
queue.add(3)
queue.add(4)
queue.add(5)
queue.add(6)
print array
print queue.take()
print array