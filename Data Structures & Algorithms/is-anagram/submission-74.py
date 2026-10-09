class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        for i in countS:
            if countS[i] != countT.get(i, 0):
                return False
        return True























        



        # count = {}

        # for i in range(len(s)):
        #     count[s[i]] = count.get(s[i],0) + 1
        #     count[t[i]] = count.get(t[i],0) - 1
        
        # for v in count.values():
        #     if v != 0:
        #         return False
        
        # return True






        