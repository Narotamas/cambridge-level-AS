class queue:
    def __init__ (self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        print ("pushed {item}")

    def is_empty(self):
        return len(self.items) == 0
    
    def length(self):
        return len(self.items)
    
    def check(self):
        if not self.is_empty():
            return self.items [1]
        else:
            return("stack is empty")
    
    def pop(self):
        