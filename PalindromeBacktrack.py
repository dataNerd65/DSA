class Solution:
    def partition(self, s: str):

        #Helper function
        #is_palindrome checks if a substring is a palindrome by comparing the string with its reverse.
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        #backtrack takes the starting index and the current path of palindromic substrings.

        def backtrack(start: int, path: list):
            #If the starting index reaches the length of the string, the current path is added to the result list res.
            if start == len(s):
                res.append(path[:])
                return
     #The loop iterates from the starting index to the end of the string, forming substrings.

     #If a substring is a palindrome, it is appended to the path, and backtrack is called recursively for the next index.
     #After exploring with the current substring, it is removed (backtracked) from the path.
       

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()
        
        #The function initializes the result list res and starts the backtracking process from index 0.
        res = []
        backtrack(0, [])
        return res
    

#Example Usage
solution = Solution()
print(solution.partition("aab"))
print(solution.partition("a"))