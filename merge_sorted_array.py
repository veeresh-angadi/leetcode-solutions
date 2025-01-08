class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #start comparing the last elements of the array , while m and n > 0
        while m>0 and n>0:
            #if last element of nums1 is >= nums2 ,place the element in m+n-1 and decrement m-1
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m-=1
            #if last element of nums2 is > nums1 ,place the element in m+n-1 and decrement n-1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1
        #if n have remaining elements , copy remaining in nums1
        if n > 0:
            nums1[:n]=nums2[:n]
        
