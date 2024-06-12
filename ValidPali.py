class Solution:
    def isPalindrome(self, s:str) -> bool:
        #initialize pointers for the start and end of the string
        left, right = 0, len(s) - 1

        #continue traversing until the pointers meet
        while left < right:
            #move the left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1

            #move the right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1

            #Compare the characters ignoring case differences
            if left < right and s[left].lower() != s[right].lower():
                return False
            
            #move the pointers towards the center
            left += 1
            right -= 1

        #if loop completes without finding any mismatch, its a palindrome
        return True
    
soln = Solution()
print(soln.isPalindrome("A man, a plan, a canal: Panama"))
print(soln.isPalindrome("race a car"))
print(soln.isPalindrome(" "))
