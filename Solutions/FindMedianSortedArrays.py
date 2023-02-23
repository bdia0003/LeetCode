import unittest

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        i,j = 0,0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1

        nums3 = nums3 + nums1[i:] + nums2[j:]

        length = len(nums3)

        if length % 2 == 0:
            return (nums3[length//2] + nums3[length//2 - 1]) / 2
        else:
            return nums3[length//2]




class TestSolution(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        solution = Solution()
        self.assertEqual(solution.findMedianSortedArrays([1,2,3], [4,5,6]), 3.5)
        self.assertEqual(solution.findMedianSortedArrays([1,2], [3,4]), 2.5)


if __name__ == '__main__':
    unittest.main()