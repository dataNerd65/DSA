class Solution:
    def maxJump(self, nums):

        #Initialize maxReachale to 0. This will store the farthest index we can reach at any point.
        maxReachable = 0

        for i in range(len(nums)):
            if i > maxReachable:
                return False
            
            maxReachable = max(maxReachable, i + nums[i])

            if maxReachable >= len(nums) -1:
                return True
            
        return maxReachable >= len(nums) -1
    
soln = Solution()
nums = [2, 3, 1, 1, 4]
print(soln.maxJump(nums))

nums2 = [3, 2, 1, 0, 4]
print(soln.maxJump(nums2))