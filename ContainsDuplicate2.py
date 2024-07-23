class Solution:
    def containsNearbyDuplicate(self, nums, k):
        #Dictionary to store the last seen index of each element
        last_seen = {}

        #Iterating through the list with index
        for i, num in enumerate(nums):
            #Checking if the number was seen before and is within the range k
            if num in last_seen and i - last_seen[num] <= k:
                return True
            
            #Update the last seen indexof the current number
            last_seen[num] = i
        
        #Return false if no such pair was found
        return False
    
soln = Solution()
print(soln.containsNearbyDuplicate([1, 2, 3, 1], 3))
print(soln.containsNearbyDuplicate([1, 0, 1, 1], 1))
print(soln.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))

    
