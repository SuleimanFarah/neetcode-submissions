class MinStack:

    def __init__(self):
        self.lst = []

    def push(self, val: int) -> None:
        if self.lst == []:
            self.lst.append((val, val))
        else:
            self.lst.append((val, min(val, self.lst[-1][1])))

    def pop(self) -> None:
        self.lst.pop()

    def top(self) -> int:
        return self.lst[-1][0]
        

    def getMin(self) -> int:
        return self.lst[-1][1]

##### 1 (1,1) - 2 (2, 1) - 0 (0, 0)