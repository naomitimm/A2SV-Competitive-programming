class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.stack == []:
            self.stack.append((val,val))
            return

        if val > self.stack[-1][1] :
            self.stack.append((val, self.stack[-1][1]))  
        else:
            self.stack.append((val, val))    

    def pop(self) -> None:
        value = self.stack.pop()
        return value[0]

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        #
        return self.stack[-1][1]
        