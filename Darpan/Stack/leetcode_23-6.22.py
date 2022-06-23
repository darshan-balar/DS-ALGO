#question link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        top = 0
        maxi = 0
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                stack.append(s[i])
                top += 1
            elif s[i] == ')':
                stack.pop()
                top = len(stack)
            else:
                pass

            if maxi < top:
                maxi = top
        return maxi


#question link: https://leetcode.com/problems/remove-outermost-parentheses/
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        stack = ['(']
        index = [0]
        new = ''
        for i in range(1, n-1):
            if len(stack) == 0:
                index.append(i-1)
                index.append(i)

            if s[i] == '(':
                stack.append(s[i])
            else:
                stack.pop()
        index.append(n-1)
        for i in range(n):
            if i not in index:
                new += s[i]
        return new


#question link: https://leetcode.com/problems/baseball-game/submissions/
class Solution:
    def calPoints(self, ops) -> int:
        stack = []
        n = len(ops)
        for i in range(n):
            if ops[i] == '+':
                stack.append(stack[-1]+stack[-2])
            elif ops[i] == 'D':
                stack.append(stack[-1]*2)
            elif ops[i] == 'C':
                stack.pop()
            else:
                stack.append(int(ops[i]))
        return sum(stack)


#question link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            if len(stack) == 0:
                stack.append(s[i])
            elif s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)


#question link: https://leetcode.com/problems/crawler-log-folder/
class Solution:
    def minOperations(self, logs) -> int:
        n = len(logs)
        count = 0
        for i in range(n):
            if logs[i] == '../':
                if count != 0:
                    count -= 1
            elif logs[i] == './':
                pass
            else:
                count += 1
        return count


#question link: https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop(0)

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
