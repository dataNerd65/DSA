class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        count = 0
        start = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                if start == current:
                    break
            start += 1

soln = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
soln.rotate(nums, k)
print(nums)
