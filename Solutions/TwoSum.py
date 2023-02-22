import unittest

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = None

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    output = [i,j]
                    break

        return output

    def twoSum_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i,hashmap[complement]]

    def twoSum_3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i,hashmap[complement]]
            hashmap[nums[i]] = i


class TestTwoSum(unittest.TestCase):
    def test_twoSum(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([2,7,11,15], 9), [0,1])
        self.assertEqual(solution.twoSum([3,2,4], 6), [1,2])
        self.assertEqual(solution.twoSum([3,3], 6), [0,1])

        self.assertEqual(solution.twoSum_3([3,3], 6), [0,1])


if __name__ == '__main__':
    unittest.main()