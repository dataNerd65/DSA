class Solution:
    def remDupInSorted(self, nums):

        if not nums:
            return 0
        
        write = 1 #Pointer to indicate where next unique or second duplicate should be placed
        count = 1 #keeps track of occurrences of an element(current)

        for current in range(1, len(nums)):
                                #pointer to previous
            if nums[current] == nums[current - 1]:
                count += 1

            else:
                count = 1
            #Allow up to 3 occurrences of the same element
            if count <= 3:
                nums[write] = nums[current]
                write += 1

        return write
    
soln = Solution()
nums = [0,0,0,0,1,1,1,2,2,3,3,3,3,4]
k = soln.remDupInSorted(nums)
print(k, nums[:k])
