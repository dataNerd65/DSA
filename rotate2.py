class Solution:
    def rotate(self, nums, k):
        #In our rotate function, define a reverse function that takes three params, the array, the start index and the end index
        #This function will reverse the elements in the array from the start index to the end index
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end -1 
        
        #in the rotate function, adjust k to be <k % len(nums)> times
        #This is because, if k is larger than the length of the array, rotating the array k times is same as rotating it
        #k % len(nums) times
        k %= len(nums)

        #calling the reverse function to reverse the whole array
        reverse(nums, 0, len(nums) - 1)

        #calling the reverse function to reverse the first k elements
        reverse(nums, 0, k-1)

        #calling the reverse function to reverse the rest of the elements
        reverse(nums, k, len(nums) - 1)

#small soln implementation but whole large documentation

soln = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
soln.rotate(nums, k)
print(nums)