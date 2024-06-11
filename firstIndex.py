class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Finds the index of the first occurrence of needle in haystack,
        or -1 if needle is not part of haystack.
        
        :param haystack: str - The string to search in
        :param needle: str - The string to search for
        :return: int - The index of the first occurrence of needle, or -1 if not found
        """
        # Check if needle is an empty string
        if not needle:
            return 0
        
        # Use the built-in find method to locate the needle in haystack
        return haystack.find(needle)

# Example to test the class method
# This is just for local testing; LeetCode will call the method as needed.
solution = Solution()
print(solution.strStr("sadbutsad", "sad"))  # Output: 0
print(solution.strStr("leetcode", "leeto"))  # Output: -1
