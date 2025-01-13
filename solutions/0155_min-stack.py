# Problem: https://leetcode.com/problems/min-stack
# Runtime: 44 ms

class MinStack(object):
    def __init__(self):
        self.minStack = []
        self.stack = []
        self.minVal = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.minVal == None or val <= self.minVal:
            self.minVal = val
            self.minStack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        ret = self.stack.pop()
        if ret == self.minVal:
            self.minStack.pop()
            if len(self.minStack) == 0:
                self.minVal = None
            else:
                self.minVal = self.minStack[len(self.minStack) - 1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack) - 1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minVal
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()