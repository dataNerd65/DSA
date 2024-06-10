class Solution:
    def maxJump(self, nums):

        #Initialize maxReachale to 0. This will store the farthest index we can reach at any point.
        maxReachable = 0

        #Iterate through the array using an index i. For each index, check if i is greater than max_reachable.
        # If it is, return false because we can't move beyond this point

        for i in range(len(nums)):
            if i > maxReachable:
                return False
            #Update max_reachable to be the maximum of its current value and i + nums[i] (the farthest we can reach from index i).

            maxReachable = max(maxReachable, i + nums[i])
            
            #If max_reachable is greater than or equal to the last index of the array at any point, 
            #return true because we can reach or surpass the last index.
            if maxReachable >= len(nums) -1:
                return True
            
        return maxReachable >= len(nums) -1
    
soln = Solution()
nums = [2, 3, 1, 1, 4]
print(soln.maxJump(nums))

nums2 = [3, 2, 1, 0, 4]
print(soln.maxJump(nums2))