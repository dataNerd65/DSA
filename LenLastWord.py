class Solution:
    def lenOfLastWord(self, s):
        #Trimming any trailing spaces to ensure the last word is correctly identified
        s = s.rstrip()

        #Split the string into a list of words
        words = s.split()

        #The last word will be the last non-empty string in the list
        lastWord = words[-1]

        return len(lastWord)
    
soln = Solution()
s = "Hello World"
s1 = "   fly me   to   the moon  "
s2 = "luffy is still joyboy"

print(soln.lenOfLastWord(s))
print(soln.lenOfLastWord(s1))
print(soln.lenOfLastWord(s2))


