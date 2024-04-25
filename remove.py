class Solution(object):
    def removeElement(self, nums, val):
        #Initialize k as 0
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# Example usage:
nums = [3, 2, 2, 3]
val = 3

solution = Solution()
result = solution.removeElement(nums, val)
print(result)
print("Modified array:", nums[:result])
print("Number of elements not equal to", val, ':', result)


