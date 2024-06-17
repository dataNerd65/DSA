from collections import defaultdict
magazineCount = defaultdict(int)

class Solution:
    def canConstruct(self, ransomNote, Magazine):
        #Creating a Hashmap to count the frequency of each character in magazine
        #magazineCount = defaultdict[int]

        #Populate the HashMap with characters from magazine
        for char in Magazine:
            magazineCount[char] += 1

        #Check if we can construct ransomNote using the magazine characters
        for char in ransomNote:
            if magazineCount[char] == 0:
                return False
            magazineCount[char] -= 1

        return True
    
soln = Solution()

print(soln.canConstruct(ransomNote="a", Magazine="b"))
print(soln.canConstruct(ransomNote="aa", Magazine="ab"))
print(soln.canConstruct(ransomNote="aa", Magazine="aab"))
