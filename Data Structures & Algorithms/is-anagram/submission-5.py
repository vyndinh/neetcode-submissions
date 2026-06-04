class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapStr1, mapStr2 = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in mapStr1:
                mapStr1[s[i]] += 1
            else:
                mapStr1[s[i]] = 1

            if t[i] in mapStr2:
                mapStr2[t[i]] += 1
            else:
                mapStr2[t[i]] = 1
        return mapStr1 == mapStr2


