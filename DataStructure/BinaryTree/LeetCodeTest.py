import math


'''There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.'''

def findMedianSortedArrays(nums1, nums2):
        
    nums1 = sorted(nums1 + nums2)
    index = int(len(nums1)/2)
    
    if (len(nums1) % 2 != 0):
        return nums1[index]
    else:
        return (nums1[index] + nums1[index-1])/2

    
nums1 = [1,7]
nums2 = [2,11]

print(findMedianSortedArrays(nums1, nums2))
