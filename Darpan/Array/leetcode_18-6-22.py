#question link: https://leetcode.com/problems/find-players-with-zero-or-one-losses/
class Solution:
    def findWinners(self, matches):
        winners = {}
        losers = {}
        for i, j in matches:
            winners[i] = 0
            losers[j] = 0
        for i, j in matches:
            winners[i] += 1
            losers[j] += 1
        lost = [i for i, j in losers.items() if j == 1]
        lost.sort()
        win = []
        for i in winners.keys():
            if i not in losers.keys():
                win.append(i)
        win.sort()
        return [win, lost]


#question link: https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, t):
        s = []
        new = []
        for i in reversed(range(len(t))):
            if(len(s) == 0):
                new.append(0)
            elif(len(s) > 0 and t[i] < s[-1][0]):
                new.append(s[-1][1] - i)
            elif(len(s) > 0 and t[i] >= s[-1][0]):
                while(len(s) > 0 and t[i] >= s[-1][0]):
                    s.pop()
                if(len(s) == 0):
                    new.append(0)
                else:
                    new.append(s[-1][1] - i)

            s.append([t[i], i])

        return new[::-1]



#question link: https://leetcode.com/problems/k-closest-points-to-origin/
class Solution:
    def kClosest(self, points, k):
        n = len(points)
        x = [(i**2 + j**2)**(0.5) for i, j in points]
        new = x[:]
        x.sort()
        x = x[:k]
        res = []
        for i in range(n):
            if new[i] in x:
                res.append(points[i])
        return res


#question link: https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
class Solution:
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)
        c = 0
        reverse = [0]*n
        for i in range(n-1, -1, -1):
            c += nums[i]
            reverse[i] = c
        neg = []
        c = 0
        for i in range(n-1):
            c -= nums[i]
            neg.append(c)
        mul = -n
        ans = []
        for i in range(n):
            if i == 0:
                x = reverse[i] + mul*nums[i]
                ans.append(x)
                mul += 2
            else:
                x = reverse[i] + mul*nums[i]+neg[i-1]
                ans.append(x)
                mul += 2
        return ans
