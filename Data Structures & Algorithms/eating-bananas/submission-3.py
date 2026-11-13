class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r)//2
            hrs = 0
            
            for p in piles:
                hrs += math.ceil(p/k)

            if hrs <= h:
                res = min(res,k)
                r = k-1
            else:
                l = k+1

        return res









        # for k in range(1, max(piles)+1):
        #     hrs = 0

        #     for i in piles:
        #         hrs += (i + k - 1) // k

        #     if hrs <= h:
        #         return k





            