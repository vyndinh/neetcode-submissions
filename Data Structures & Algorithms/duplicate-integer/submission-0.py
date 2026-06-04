class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapNums = {}
        
        for n in nums:
            if n in mapNums:
                return True
            mapNums[n] = 1
        return False