#question link: https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1, m, nums2, n ):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new = []
        nums = nums1[:m]
        numss = nums2[:n]
        i = 0
        j = 0
        while i < m and j < n:
            if nums[i] > numss[j]:
                new.append(numss[j])
                j += 1
            else:
                new.append(nums[i])
                i += 1
        if i < len(nums):
            new.extend(nums[i:])
        else:
            new.extend(numss[j:])
        for i in range(m+n):
            nums1[i] = new[i]


#question link: https://leetcode.com/problems/maximum-average-subarray-i/
class Solution:
    def findMaxAverage(self, nums, k):
        n = len(nums)
        if n < k:
            return sum(nums)/len(nums)
        summ = sum(nums[:k])
        maxi = summ/k
        j = 0
        while j < n-k:
            summ = summ+nums[j+k]-nums[j]
            new = summ/k
            if new > maxi:
                maxi = new
            j += 1
        return maxi


#question link: https://leetcode.com/problems/valid-boomerang/
class Solution:
    def isBoomerang(self, points):
        (x1, y1), (x2, y2), (x3, y3) = points
        return (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)


#question link: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
class Solution:
    def numberOfBeams(self, bank):
        value = []
        for i, obj in enumerate(bank):
            new = sum(1 for i in obj if i == '1')
            if new != 0:
                value.append(new)
        if len(value) <= 1:
            return 0
        n = len(value)-1
        summ = 0
        for i in range(n):
            summ += value[i]*value[i+1]
        return summ


#question link: https://leetcode.com/problems/rearrange-array-elements-by-sign/
class Solution:
    def rearrangeArray(self, nums):
        pos = []
        neg = []
        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        j = 0
        k = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = pos[j]
                j += 1
            else:
                nums[i] = neg[k]
                k += 1
        return nums


#question link: https://leetcode.com/problems/finding-the-users-active-minutes/
class Solution:
    def findingUsersActiveMinutes(self, logs, k):
        maps = {}
        for i in range(len(logs)):
            maps[logs[i][0]] = []
        for i in range(len(logs)):
            maps[logs[i][0]].append(logs[i][1])
        ans = [0]*k
        new = []
        for i in maps.values():
            i = set(i)
            new.append(len(i))
        res = {}
        for i in new:
            res[i] = 0
        for i in new:
            res[i] += 1
        for i in res.keys():
            if res[i] == i:
                ans[i-1] = i
            else:
                ans[i-1] = res[i]
        return ans
