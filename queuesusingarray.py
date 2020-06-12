class QueueUsingStack():
    def __init__(self):
        self.data = {}
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def push(self,item):
        self.data[self.length] = item
        self.length += 1
        return self.data

    def pop(self):
        index = 0
        item = self.data[index]
        self.shiftItems(index)

    def shiftItems(self,index):
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length-=1
        return self.data
    
    def peek(self):
        return self.data[0]

m = QueueUsingStack()
m.push(10)
m.push(11)
m.push(12)
m.push(13)
print(m.peek())
m.pop()
print(m.peek())
print(m)