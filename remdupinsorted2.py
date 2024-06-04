class Solution:
    def remDuplicates(self, nums):
        #The pupose of this method is to remove duplicates in a sorted array such that each element appears at most twice
        #It modifies the input array in-place and returns the new length of the array after duplicates are removed

        #if the input list of nums is empty, return 0
        if not nums:
            return 0
        
        write = 1 #Pointer to indicate where next unique or second duplicate should be placed
        #write stands at index 1
        count = 1 # count of occurrences of current element

        #Iterating over the list starting from second element and if current element is same as previous one, it increments count
        for current in range(1, len(nums)):
                                #previous
            if nums[current] == nums[current - 1]:
                count += 1

            #If the current element is different from previous one, reset count to 1
            else:
                count = 1
            
            #If count is less than or equal to 2, meaning is either unique or a duplicate(second) it places current element
            #at the position indicated by write and then increments write

            if count <= 2:
                nums[write] = nums[current]
                write += 1

        return write #The new length of the array after duplicates have been removed
    
soln = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = soln.remDuplicates(nums)
print(k, nums[:k])

nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
k1 = soln.remDuplicates(nums2)
print(k1, nums2[:k1]) #Be keen

#Due to the fact that in some languages the array length is not changeable,  you must instead have the result be placed in the first part of the array nums
#Be keen not to make mistakes