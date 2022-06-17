import math
# question link: https://leetcode.com/problems/partition-array-for-maximum-sum/

class Solution:
    def maxSumAfterPartitioning(self, arr, k):
        n = len(arr)
        dp = [0]*n

        for j in range(k):
            dp[j] = max(arr[:j+1])*(j+1)

        for j in range(k, n):
            curr = []
            for m in range(k):
                curr.append(dp[j-m-1] + max(arr[(j-m):(j+1)]) * (m+1))
            dp[j] = max(curr)

        return dp[-1]


# question link: https://leetcode.com/problems/stone-game/
class Solution:
    def stoneGame(self, piles):
        return True   #we can mathematically prove that alice always wins 


#question link: https://leetcode.com/problems/reduce-array-size-to-the-half/
class Solution:
    def minSetSize(self, arr):
        n = len(arr)
        maps = {}
        for i in arr:
            maps[i] = 0
        for i in arr:
            maps[i] += 1
        new = sorted(maps.values(), reverse=True)
        x = len(new)
        i = 0
        count, counter = 0, 0
        while i < x:
            count += new[i]
            counter += 1
            if count >= n//2:
                break
            i += 1
        return counter


#question link: https://leetcode.com/problems/minimum-falling-path-sum/
class Solution:
    def minFallingPathSum(self, m):
        n = len(m)

        if n == 1:
            return m[0][0]

        for i in range(n-2, -1, -1):
            for j in range(n-1, -1, -1):
                bottom = m[i+1][j]
                bottom_left = m[i+1][j-1] if j-1 >= 0 else math.inf
                bottom_right = m[i+1][j+1] if j+1 < n else math.inf
                m[i][j] += min(bottom, bottom_left, bottom_right)

        return min(m[0])

