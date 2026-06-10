import random
class Solution:
    def swap(self,nums, i, j):
        tp = nums[i]
        nums[i] = nums[j]
        nums[j] = tp       
    def partition(self,nums, pivot):
        left = -1
        right = len(nums)
        i = 0
        while i < right:
            if nums[i] < pivot:
                left += 1
                self.swap(nums, left, i)
                i += 1
            elif nums[i] == pivot:
                i += 1
            else:
                right -= 1
                self.swap(nums, right, i) 
        return [left + 1, right - 1]
   
    def findKthLargest(self, nums: List[int], k: int) -> int:
        index = len(nums) - k
        l, r = 0, len(nums) - 1
        while l <= r:
            pivot = nums[random.randint(l, r)]
            range = self.partition(nums, pivot)

            start = range[0]
            end = range[1]

            if index >= start and index <= end:
                return pivot
            elif index < start:
                r = start - 1
            else:
                l = end + 1

        return -1

    

        # def quickSort(nums):
        #     if len(nums) <= 0:
        #         return None
        #     pivot = nums[-1]
        #     l = []
        #     r = []
        #     for i in range(len(nums)-1):
        #         if nums[i] < pivot:
        #             l.append(nums[i])
        #         elif nums[i] >= pivot:
        #             r.append(nums[i])
        #     if len(r) == self.indx:
        #         return r[0]
        #     elif len(r) > self.indx:
        #         quickSort(r)
        #     else:
        #         quickSort(l)
        # return quickSort(nums)
