class Array1D:
    def __init__(self, length):
        self.length = length
        self.__array = [0] * length
        self.size = 0

    def getArray(self):
        return self.__array[:self.size]  # Return only the active elements

    def append(self, num):
        if self.isFull():
            print("Array is full. Cannot append.")
            return
        self.__array[self.size] = num
        self.size += 1

    def insert(self, value, index):
        if self.isFull():
            print("Array is full. Cannot insert.")
            return
        if index < 0 or index > self.size:
            print("Invalid index.")
            return
        for i in range(self.size, index, -1):
            self.__array[i] = self.__array[i-1]
        self.__array[index] = value
        self.size += 1

    def deleteAt(self, index):
        if self.isEmpty():
            print("Array is empty. Cannot delete.")
            return
        if index < 0 or index >= self.size:
            print("Invalid index.")
            return
        for i in range(index, self.size - 1):
            self.__array[i] = self.__array[i + 1]
        self.size -= 1
        self.__array[self.size] = 0  # Clear the last element

    def deleteValue(self, value):
        if self.isEmpty():
            print("Array is empty. Cannot delete.")
            return
        for i in range(self.size):
            if self.__array[i] == value:
                self.deleteAt(i)
                return
        print("Value not found.")

    def deleteBegin(self):
        self.deleteAt(0)

    def deleteEnd(self):
        if not self.isEmpty():
            self.size -= 1
            self.__array[self.size] = 0
        else:
            print("Array is empty. Cannot delete.")

    def traversal(self):
        if self.isEmpty():
            print("Array is empty.")
        else:
            print("Array elements:", self.getArray())

    def isFull(self):
        return self.size == self.length

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size


