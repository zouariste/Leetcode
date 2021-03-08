class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        if not nums or not (1 in nums):
            return 1
        for i in range(n):
            if (nums[i] == 0 or nums[i] < 0 or nums[i] > n):
                nums[i] = 1
        for i in range(n):
            j = abs(nums[i])
            nums[j-1] = - abs(nums[j-1])
        for i in range(n):
            if (nums[i] > 0):
                return i+1
        return n + 1
