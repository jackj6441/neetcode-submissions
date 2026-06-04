class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        total = len(A)+len(B)
        half = (total)//2
        l, r = 0, len(A)
        while True:
            i = (r+l)//2
            j = half - i
            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")

            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")
            if Aleft <= Bright and Aright >= Bleft:
                if total % 2 == 0:
                    return (max(Aleft,Bleft) + min(Aright,Bright))/2
                else:
                    return min(Aright,Bright)
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        return 0.0
        
        
            