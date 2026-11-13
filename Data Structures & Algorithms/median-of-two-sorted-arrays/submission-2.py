class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       # we need O(log(m+n))
       
        # below is O(m+n) 
        nums = nums1 + nums2

        nums.sort()

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2

            if len(nums) % 2 != 0:
                return nums[m]
            else:
                return ((nums[m] + nums[m+1])/2)