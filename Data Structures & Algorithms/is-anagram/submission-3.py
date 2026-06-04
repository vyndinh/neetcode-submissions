class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     mapStr1, mapStr2 = {}, {}

    #     for i in range(len(s)):
    #         if s[i] in mapStr1:
    #             mapStr1[s[i]] += 1
    #         else:
    #             mapStr1[s[i]] = 1

    #         if t[i] in mapStr2:
    #             mapStr2[t[i]] += 1
    #         else:
    #             mapStr2[t[i]] = 1
    #     return mapStr1 == mapStr2


    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            if s[i] in countS:
                countS[s[i]] += 1
            else:
                countS[s[i]] = 1

            if t[i] in countT:
                countT[t[i]] += 1
            else:
                countT[t[i]] = 1

        return countS == countT
