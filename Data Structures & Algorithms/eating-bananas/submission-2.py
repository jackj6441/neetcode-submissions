class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1
        l,r = 1, max(piles)
        while l <= r:
            check = 0
            mid = (r+l)//2
            for a in piles:
                check += math.ceil(float(a)/mid)
            if check <= h:
                r = mid - 1
                speed = mid
            else:
                l = mid + 1
        return speed