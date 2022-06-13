from collections import Counter
#question link : https://leetcode.com/problems/two-out-of-three/
class Solution:
    def twoOutOfThree(self, nums1 , nums2, nums3):
        nums1.sort()
        nums2.sort()
        nums3.sort()
        ans = []
        def intersection(A, B):
            a = len(A)
            b = len(B)
            i, j = 0, 0
            while i < a and j < b:
                if A[i] == B[j]:
                    ans.append(A[i])
                    i += 1
                    j += 1
                elif A[i] > B[j]:
                    j += 1
                else:
                    i += 1
        intersection(nums1, nums2)
        intersection(nums2, nums3)
        intersection(nums1, nums3)
        maps = {}
        for i in ans:
            maps[i] = 0
        return list(maps.keys())



# question link: https://leetcode.com/problems/kth-distinct-string-in-an-array/
class Solution:
    def kthDistinct(self, arr, k):
        maps = {}
        for i in arr:
            maps[i] = 0
        for i in range(len(arr)):
            maps[arr[i]] += 1
        x = [i for i, j in maps.items() if j == 1]
        if k > len(x):
            return ''
        return x[k-1]




#question link: https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
class Solution:
    def minCostToMoveChips(self, position):
        even = 0
        odd = 0
        for i in position:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)



#question link: https://leetcode.com/problems/maximum-units-on-a-truck/
class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        new = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        cost = 0
        count = 0
        i = 0
        while count <= truckSize and i < len(new):
            cost += new[i][0]*new[i][1]
            count += new[i][0]
            index = new[i][1]
            i += 1
        if i <= len(new) and count > truckSize:
            cost -= (count-truckSize)*index
        return cost


#question link: https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = -nums[i]
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        return nums



#question link: https://leetcode.com/problems/build-an-array-with-stack-operations/
class Solution:
    def buildArray(self, target, n):
        new = []
        check = list(range(1, n+1))
        k = len(target)
        j = 0
        for i in range(k):
            if target[i] == check[j]:
                new.append("Push")
                j += 1
            else:
                for _ in range(target[i]-check[j]):
                    new.append("Push")
                    new.append("Pop")
                    j += 1
                new.append("Push")
                j += 1
        return new


#question link: https://leetcode.com/problems/sort-array-by-parity-ii/
class Solution:
    def sortArrayByParityII(self, nums):
        even = []
        odd = []
        n = len(nums)
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        ans = []
        i = 0
        j = 0
        k = 0
        while i < n:
            if i % 2 == 0:
                ans.append(even[j])
                j += 1
            else:
                ans.append(odd[k])
                k += 1
            i += 1
        return ans


#question link: https://leetcode.com/problems/finding-3-digit-even-numbers/
class Solution:
    def findEvenNumbers(self, digits):
        ans = []
        count = Counter(digits)
        for a in range(1, 10):
            for b in range(0, 10):
                for c in range(0, 9, 2):
                    if count[a] > 0 and count[b] > (b == a) and count[c] > (c == a)+(c == b):
                        ans.append(a*100+b*10+c)
        return ans


#question link: https://leetcode.com/problems/range-sum-query-immutable/
class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        return sum(self.nums[left:right+1])
    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)



