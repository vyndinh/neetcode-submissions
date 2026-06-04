class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)

        for num in nums:
            curr = num
            count = 0
            while curr in numset:
                curr += 1
                count += 1
            res = max(res, count)
        return res