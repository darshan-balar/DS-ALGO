#question link: https://leetcode.com/problems/make-the-string-great/
class Solution:
    def makeGood(self, s: str) -> str:
        new = list(s)
        i = 0
        while i < len(new)-1:
            if new[i] != new[i+1] and (new[i+1].upper() == new[i] or new[i+1].lower() == new[i]):
                new = new[:i] + new[i+2:]
                i = 0
            else:
                i += 1
        return ''.join(new)
    
 
 
    
#question link: https://leetcode.com/problems/min-stack/
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()





#question link: https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        types = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] in types.keys():
                stack.append(s[i])
            else:
                if len(stack) != 0 and s[i] == types[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
    
  
  
    
#question link: https://leetcode.com/problems/backspace-string-compare/
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        stack1 = []
        stack2 = []
        count1 = 0
        count2 = 0
        for i in range(n1):
            if s[i] == '#':
                if count1 != 0:
                    stack1.pop()
                    count1 -= 1
            else:
                stack1.append(s[i])
                count1 += 1
        for i in range(n2):
            if t[i] == '#':
                if count2 != 0:
                    stack2.pop()
                    count2 -= 1
            else:
                stack2.append(t[i])
                count2 += 1

        return stack1 == stack2
    
    
    
    

#question link: https://leetcode.com/problems/design-a-stack-with-increment-operation/
class CustomStack:

    def __init__(self, maxSize: int):
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if len(self.inc) == 0:
            return -1
        else:
            return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.inc))):
            self.inc[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)



