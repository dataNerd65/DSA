class Solution:
    #The purpose of the following method is to find the majority element in an array
    def MajorityElement(self, nums):
        #candidate variable is used to store current candidate for the majority element
        candidate = None

        #count variable counts occurrences of the candidate
        count = 0
        
        #Iterating over the list
        for num in nums:
            #if count == 0, it sets current no. as candidate and sets count to 1
            if count == 0:
                candidate = num
                count = 1
            
            #If current no. is the same as candidate , it increments count

            elif num == candidate:
                count += 1
                #if differnt , decrement count
            else:
                count -= 1
            
        #After iteration over all elements, candidate will be the majority element

        return candidate
    
soln = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
print(soln.MajorityElement(nums))


nums2 =[3, 2, 3]
print(soln.MajorityElement(nums2))

