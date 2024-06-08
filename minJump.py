class Solution:
    def minJump(self, nums):

        n = len(nums)
        if n == 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

                if current_end >= n - 1:
                    break
        return jumps
    
soln = Solution()

nums = [2, 3, 1, 1, 4]
nums2 = [2, 3, 0, 1, 4]
print(soln.minJump(nums))
print(soln.minJump(nums2))
