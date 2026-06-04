class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest_streak = 0

        for num in nums:
            if num - 1 not in numset:
                curr = num
                current_streak = 1

                while curr + 1 in numset:
                    current_streak += 1
                    curr += 1
                longest_streak = max(current_streak, longest_streak)
        return longest_streak
        