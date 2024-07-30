class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        
        # Lists to keep track of the sum and count of nodes at each level
        sums = []
        counts = []

        # Helper function for DFS
        def dfs(node, depth):
            if not node:
                return
            
            # If we are at a new depth, initialize sums and counts
            if depth == len(sums):
                sums.append(node.val)
                counts.append(1)
            else:
                sums[depth] += node.val
                counts[depth] += 1
            
            # Recur for left and right children
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        # Start DFS traversal from the root
        dfs(root, 0)

        # Calculate averages
        averages = [s / c for s, c in zip(sums, counts)]
        return averages

# Example usage:
# Constructing the tree [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.averageOfLevels(root))  # Output: [3.0, 14.5, 11.0]
