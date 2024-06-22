class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        # Dictionaries to keep track of the mapping
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            # Check if there is an existing mapping for char_s to char_t
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                # Before creating a new mapping, ensure char_t is not already mapped to a different char_s
                if char_t in t_to_s and t_to_s[char_t] != char_s:
                    return False
                # Create new mapping
                s_to_t[char_s] = char_t
                t_to_s[char_t] = char_s

        return True

soln = Solution()
print(soln.isIsomorphic("egg", "add"))  # True
print(soln.isIsomorphic("foo", "bar"))  # False
print(soln.isIsomorphic("paper", "title"))  # True