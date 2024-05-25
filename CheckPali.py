class Solution(object):
    def checkPali(self, x):
        #If number is -ve or (if its not o but ends with zero) not a palindrome
        if x < 0 or (x !=0 and x % 10 == 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return x == reversed_half or x == reversed_half // 10
    
soln = Solution()
print (soln.checkPali(12321))