#question link: https://leetcode.com/problems/watering-plants/
class Solution:
    def wateringPlants(self, plants, capacity):
        steps = 0
        n = len(plants)
        count = capacity
        for i in range(n):
            steps += 1
            count -= plants[i]
            if i != n-1 and count < plants[i+1]:
                steps += 2*(i+1)
                count = capacity

        return steps


#question link: https://leetcode.com/problems/find-triangular-sum-of-an-array/
class Solution:
    def triangularSum(self, nums):
        def solution(l):
            n = len(l)
            if n == 1:
                return l[0]
            else:
                x = []
                for i in range(n-1):
                    x.append((l[i]+l[i+1]) % 10)
                return solution(x)
        return solution(nums)



#question link: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
class Solution:
    def maxCoins(self, piles):
        n = len(piles)
        piles.sort()
        summ = 0
        i = n-2
        count = 0
        while i >= 0 and count < n//3:
            summ += piles[i]
            i -= 2
            count += 1
        return summ


