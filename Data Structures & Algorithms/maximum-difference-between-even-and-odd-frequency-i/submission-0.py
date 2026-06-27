class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0] * 26
        
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        max_odd  = 0
        min_even = float('inf')
        
        for count in freq:
            if count == 0:
                continue
            if count % 2 == 1:
                max_odd = max(max_odd, count)
            else:
                min_even = min(min_even, count)
        
        return max_odd - min_even