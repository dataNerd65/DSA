class Solution:
    def isHappy(self, n):
        def sumOfSquares(num):
            return sum(int(digit) ** 2  for digit in str(num))
        
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = sumOfSquares(n)

        return n == 1
    
soln = Solution()
print(soln.isHappy(19))
print(soln.isHappy(2))
