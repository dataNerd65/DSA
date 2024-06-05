class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k  %= n
        nums[:] = nums[-k:] + nums[:-k]


soln = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
soln.rotate(nums, k=3)
print(nums)
        