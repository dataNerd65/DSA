class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k  %= n

        #nums[-k:] slices the list from the -k index to the end of the list
        #in python, negative indexing starts from the end of the list, so nums[-k:] gets the last k elements of the list
        #nums[:-k] slices the list from the start of the list to the -k index. in short, it gets all the elements except for the last k elements
        #nums[-k:] + nums[:-k] concatenates the modified list
        #nums[:] = ... assigns the result back to nums
        nums[:] = nums[-k:] + nums[:-k]


soln = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
soln.rotate(nums, k=3)
print(nums)

        