class Solution:
    def twoSum(self, nums, target: int):
        n = len(nums)
        indices = []

        for i in range(n):
            for j in range(1, n):
                if (i == j):
                    continue
                
                if (nums[i] + nums[j]) == target:
                    indices.append(i)
                    indices.append(j)
                    return indices

        return indices
