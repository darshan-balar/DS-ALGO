#question link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution(object):
    def minAddToMakeValid(self, S):
        ans, bal = 0, 0
        for symbol in S:
            if symbol == '(':
                bal += 1
            else:
                bal -= 1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal


#question link: https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
class Solution:
    def maxDepthAfterSplit(self, seq: str):
        ans = []
        l, r = 0, 0
        n = len(seq)
        for i in range(n):
            if seq[i] == '(':
                ans.append(l)
                l = 1-l
            else:
                ans.append(r)
                r = 1-r
        return ans



#question link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s, n, st = list(s), len(s), []
        l, r = 0, n-1
        for i in range(n):
            if s[i] == '(':
                st.append(i)
            elif s[i] == ')':
                if st:
                    st.pop()
                else:
                    s[i] = ''
        while st:
            s[st.pop()] = ''

        return ''.join(s)


#question link: https://leetcode.com/problems/score-of-parentheses/
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        count = 0
        ans = 0
        for i in range(n):
            if s[i] == '(':
                count += 1
            else:
                count -= 1
                if s[i-1] == '(':
                    ans += 1 << count
        return ans
