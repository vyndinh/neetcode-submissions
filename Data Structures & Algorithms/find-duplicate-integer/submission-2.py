class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = fast = nums[0]

        while True:
            low = nums[low]
            fast = nums[nums[fast]]
            if low == fast:
                break
        low = nums[0]
        while low != fast:
            low = nums[low]
            fast = nums[fast]
        return fast

    
