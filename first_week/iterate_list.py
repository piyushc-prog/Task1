class reverse:
    def __init__(self,items):
        self.items = items
        self.index = len(self.items)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        
        self.index -= 1
        return self.items[self.index]

li = [1,2,3,4,5]
call_rev = reverse(li)

for i in call_rev:
    print(i)