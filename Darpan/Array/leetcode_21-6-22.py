#question link: https://leetcode.com/problems/max-consecutive-ones/
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maxi = 0
        count = 0
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 1:
                count += 1
            else:
                if maxi < count:
                    maxi = count
                count = 0
            i += 1

        if count > maxi:
            maxi = count
        return maxi


#question link: https://leetcode.com/problems/tuple-with-same-product/
class Solution:
    def tupleSameProduct(self, nums):
        n = len(nums)
        maps = {}
        for i in range(n-1):
            for j in range(i+1, n):
                maps[nums[i]*nums[j]] = 0
        for i in range(n-1):
            for j in range(i+1, n):
                maps[nums[i]*nums[j]] += 1

        return 8*(sum((x-1)*(x)//2 for _, x in maps.items() if x > 1))


#question link: https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/
class Solution:
    def findLonely(self, nums):
        n = len(nums)
        maps = {}
        for i in nums:
            maps[i] = 0
        for i in nums:
            maps[i] += 1
        ans = []
        for i, j in maps.items():
            if j == 1 and i+1 not in maps.keys() and i-1 not in maps.keys():
                ans.append(i)
        return ans


#question link: https://leetcode.com/problems/single-element-in-a-sorted-array/
class Solution:
    def singleNonDuplicate(self, nums):
        low = 0
        high = len(nums)-2
        while low <= high:
            mid = (low+high)//2
            if (mid % 2 == 0):
                if nums[mid] != nums[mid+1]:
                    high = mid - 1
                else:
                    low = mid+1
            else:
                if nums[mid] == nums[mid+1]:
                    high = mid - 1
                else:
                    low = mid + 1

        return nums[low]
