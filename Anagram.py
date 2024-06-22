class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        #create a list to count characters (26 letters for lowercase English)
        count = [0] * 26

        for char_s, char_t in zip(s, t):
            count[ord(char_s) - ord('a')] += 1
            count[ord(char_t) - ord('a')] -= 1

        #Check if all counts are 0
        return all(c == 0 for c in count)
    
soln = Solution()
print(soln.isAnagram("anagram", "nagaram"))
print(soln.isAnagram("rat", "tar"))
print(soln.isAnagram("rat", "car"))
