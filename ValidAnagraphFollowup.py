class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False
            
        return all(value == 0 for value in count.values())
    

soln = Solution()
print(soln.isAnagram("こんにちは", "こんばんは"))
print(soln.isAnagram("anagram", "nagaram"))
print(soln.isAnagram("rat", "tar"))
print(soln.isAnagram("rat", "car"))
print(soln.isAnagram("你好", "好你"))
