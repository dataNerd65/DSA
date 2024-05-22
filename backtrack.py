class subsetsInPy:
    def subsets(nums):
        def backtrack(start, path):
            #Appending the current subset to result

            res.append(path[:])
            #Exploring further elements to add to current subset
            for i in range(start, len(nums)):
                #Include nums in current subset
                path.append(nums[i])
                #Recurse with updated path and next start index
                backtrack(i + 1, path)
                #backtracking by removing last element
                path.pop()

        res = []
        backtrack(0, [])
        return res
# Example usage:
print(subsetsInPy.subsets([1, 2, 3]))
print(subsetsInPy.subsets([0]))