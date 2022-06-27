#question link: https://leetcode.com/problems/next-greater-element-ii/
class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = []
        maxi = max(nums)
        i = 0
        while i < n:
            if nums[i] == maxi:
                ans.append(-1)
            else:
                j = (i+1) % n
                while nums[j] <= nums[i]:
                    j = (j+1) % n
                ans.append(nums[j])
            i += 1
        return ans




#question link: https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/
class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            if 'abc' in s:
                s = s.replace('abc', '')
                continue
            elif len(s) == 0:
                return True
            else:
                return False



#question link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack, cur = [], ""
        for c in s:
            if cur and c != cur[-1]:
                stack.append(cur)
                cur = ""
            cur += c
            while len(cur) >= k:
                if not stack:
                    cur = ""
                    break
                cur = stack.pop()
        stack.append(cur)
        return "".join(stack)


#question link: https://leetcode.com/problems/clumsy-factorial/
class Solution:
    def clumsy(self, n: int) -> int:
        s = [-1]
        for i in range(n):
            if i % 4 == 0:
                s[-1] *= -(n-i)
            elif i % 4 == 1:
                s[-1] *= n-i
            elif i % 4 == 2:
                s[-1] = int(s[-1]/(n-i))
            else:
                s[-1] += n-i
                s.append(1)

        return sum(s) if n % 4 else sum(s)-1
