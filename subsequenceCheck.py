class Solution:
    def isSubsequence(self, s, t):
        #initializing two pointers for s and t
        s_pointer , t_pointer = 0, 0

        #Iterate over t
        while t_pointer < len(t):
            #if characters match, move s pointer
            if s_pointer < len(s) and s[s_pointer] == t[t_pointer]:
                s_pointer += 1

            #Always move t_pointer
            t_pointer += 1

        #if s pointer reached the end of s, all chars were found in t
        return s_pointer == len(s)
    
soln = Solution()
print(soln.isSubsequence("abc", "ahbgdc"))
print(soln.isSubsequence("axc", "ahbgdc"))
#be keen