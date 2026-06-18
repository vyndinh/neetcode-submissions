class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0
        count_math = 0
        
        while p2 < len(t) and p1 < len(s):
            print(s[p1])
            print(t[p2])
            if s[p1] == t[p2]:
                p1 += 1
                count_math += 1
            p2 += 1
        return count_math == len(s)
            