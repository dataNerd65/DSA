class Solution:
    def repeatedSubtsring(self, s):
        #creating a new string by concatenating s with itself and removing the first and last character

        s2 = (s + s)[1:-1]

        #Check if the original string is a substring of this new string

        return s in s2
    
soln = Solution()
s = "abab"
s2= "aba"
s3 = "abcabcabcabc"
print(soln.repeatedSubtsring(s))
print(soln.repeatedSubtsring(s2))
print(soln.repeatedSubtsring(s3))
    
