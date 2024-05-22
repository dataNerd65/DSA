class Solution:
    def partition(self, s: str):
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        

        def backtrack(start: int, path: list):
            if start == len(s):
                res.append(path[:])
                return
            

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()


        res = []
        backtrack(0, [])
        return res
    

#Example Usage
solution = Solution()
print(solution.partition("aab"))
print(solution.partition("a"))