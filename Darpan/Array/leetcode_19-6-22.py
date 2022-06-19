# question link: https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums, k):
        n = len(nums)
        maps = {}
        for i in nums:
            maps[i] = 0
        for i in nums:
            maps[i] += 1
        new = sorted(maps.items(), key=lambda x: x[1], reverse=True)
        return [new[x][0] for x in range(n) if x < k]


#question link: https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums):
        c = 1
        d = 1
        n = len(nums)
        left, right = [], [1]*n
        for i in range(n):
            c *= nums[i]
            d *= nums[n-i-1]
            left.append(c)
            right[n-i-1] = d
        ans = []
        ans.append(right[1])
        for i in range(2, n):
            ans.append(right[i]*left[i-2])
        ans.append(left[-2])
        return ans


#question link: https://leetcode.com/problems/two-city-scheduling/
class Solution:
    def twoCitySchedCost(self, costs):
        new = sorted(costs, key=lambda cost: cost[0] - cost[1])
        n = len(costs)//2
        summ = 0
        for i in range(n):
            summ += new[i][0]+new[2*n-i-1][1]
        return summ


#question link: https://leetcode.com/problems/maximum-ice-cream-bars/
class Solution:
    def maxIceCream(self, costs, coins):
        costs.sort()
        n = len(costs)
        count = 0
        summ = 0
        for i in range(n):
            if summ + costs[i] <= coins:
                summ += costs[i]
                count += 1
            else:
                break
        return count

