class Solution:
    def two_sums(self, nums, target):
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

#Example
solution= Solution()
print(solution.two_sums([2, 7, 11, 15], 9))   
print(solution.two_sums([3, 2, 4], 6))  
  