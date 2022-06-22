#question link: https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(self, matrix):
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


#question link: https://leetcode.com/problems/simple-bank-system/
class Bank:

    def __init__(self, balance):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money) -> bool:
        if account1 <= len(self.balance) and account2 <= len(self.balance):
            if self.balance[account1-1] >= money:
                self.balance[account1-1] -= money
                self.balance[account2-1] += money
                return True
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account > len(self.balance):
            return False
        self.balance[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > len(self.balance):
            return False
        if self.balance[account-1] >= money:
            self.balance[account-1] -= money
            return True
        return False
    
# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)


#question link: https://leetcode.com/problems/sum-of-even-numbers-after-queries/
class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        n = len(nums)
        ans = []
        summ = sum(i for i in nums if i % 2 == 0)
        x = len(queries)
        i = 0
        while i < x:
            count = nums[queries[i][1]]
            if count % 2 == 0:
                summ -= count
            nums[queries[i][1]] += queries[i][0]
            if (nums[queries[i][1]]) % 2 == 0:
                summ += nums[queries[i][1]]
            ans.append(summ)
            i += 1
        return ans
