import time

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
                if count[char] == 0:
                    del count[char]
            else:
                return False

        return len(count) == 0

# Example usage
s = "anagram"
t = "nagaram"

solution = Solution()

start_time = time.time()
result = solution.isAnagram(s, t)
end_time = time.time()

print(f"Result: {result}")
print(f"Runtime: {end_time - start_time} seconds")
