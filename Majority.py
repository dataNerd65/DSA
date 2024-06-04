class Solution:
    def MajorityElement(self, nums):
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
                count = 1

            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
    
soln = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
print(soln.MajorityElement(nums))


nums2 =[3, 2, 3]
print(soln.MajorityElement(nums2))
