class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        marge=[]
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i]< nums2[j]:
                marge.append(nums1[i])

                i+=1
            else:
                marge.append(nums2[j])
                j+=1

        while i < len(nums1):
            marge.append(nums1[i])
            i+=1
        while j < len(nums2):
            marge.append(nums2[j])
            j+=1


        n = len(marge)

        if n%2==1:
            return marge[n//2]

        else:
            return (marge[n//2-1]+marge[n//2])/2
 
        