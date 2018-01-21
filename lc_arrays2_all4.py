#!/usr/bin/python
# -*- coding:utf-8 -*-
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        length = len(nums1)
        if(length%2==0):
            return (nums1[int(length/2)-1]+nums1[int(length/2)])/2.0
        else:
            return nums1[int(length/2)]
#测试用例
li1 = [1,2,4,]
li2=[6,]
obj = Solution()
median=obj.findMedianSortedArrays(li1,li2)
print(median)
