class Solution():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
 
    def pop(self):
        stack1_len = len(self.stack1)
        stack2_len = len(self.stack2)
        if (stack2_len==0):
            for i in range(stack1_len):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()
         
        # return xx