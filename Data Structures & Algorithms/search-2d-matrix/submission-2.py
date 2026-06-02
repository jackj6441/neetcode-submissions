class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums: List[int], target: int) -> int:
            l,r = 0 , len(nums)-1
            while l <= r:
                mid = (r-l)//2 + l
                cur = nums[mid]
                if target == cur:
                    return True
                elif target > cur:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        
        h,w = len(matrix), len(matrix[0])
        l,r = 0 , h - 1
        while l <= r:
            mid = (r-l)//2 + l
            cur = matrix[mid][w-1]
            if target == cur:
                return True
            elif target > cur:
                l = mid + 1
            else:
                r = mid - 1
        if l == h:
            return False
        return search(matrix[l],target)
        