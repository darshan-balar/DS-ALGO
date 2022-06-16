# question link: https://leetcode.com/problems/find-the-winner-of-the-circular-game/
class Solution(object):
    def findTheWinner(self, n, k):
        Arr = list(range(1, n + 1))
        length = len(Arr)
        ref = 0

        while Arr:
            rem = (ref + k - 1) % length
            ans = Arr.pop(rem)
            ref = rem
            length -= 1

        return ans


#question link: https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums):
        def powerset(l):
            if len(l) == 0:
                return [[]]
            else:
                first = l[0]
                rest = powerset(l[1:])
                new = []
                for subset in rest:
                    new.append(subset + [first])
                return rest+new
        return powerset(nums)



#question link: https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums):
        def perm(arr):
            if len(arr) <= 1:
                return [arr]
            else:
                ans = []
                n = len(arr)
                for i in range(n):
                    new = arr[i]
                    rem = arr[:i]+arr[i+1:]
                    for j in perm(rem):
                        ans.append([new]+j)
                return ans
        return perm(nums)


#question link: https://leetcode.com/problems/queens-that-can-attack-the-king/
class Solution:
    def queensAttacktheKing(self, queens, king):
        result = []
        seen = [[False for _ in range(8)] for _ in range(8)]  

        for queen in queens:
            seen[queen[0]][queen[1]] = True
        directions = [-1, 0, 1]

        for dx in directions:
            for dy in directions:  
                if dx == 0 and dy == 0:
                    continue
                x = king[0]
                y = king[1]

                while x + dx >= 0 and x + dx < 8 and y + dy >= 0 and y + dy < 8:
                    x = x + dx
                    y = y + dy
                    if seen[x][y]:
                        result.append([x, y])
                        break
        return result



#question link: https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
class Solution:
    def partitionArray(self, nums, k):
        count, diff = 0, -1
        nums.sort()
        for i in nums:
            if i > diff:
                diff = i + k
                count += 1
        return count
