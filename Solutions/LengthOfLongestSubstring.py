import unittest

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        curr = 0
        max_substring = 0
        start = 0
        for i in range(len(s)):
            if s[i] in hashmap and hashmap[s[i]] >= start:
                index = hashmap[s[i]]
                start = index + 1
                curr = i - index
                hashmap[s[i]] = i
            else:
                hashmap[s[i]] = i
                curr += 1
                if max_substring < curr: max_substring = curr
        
        return max_substring


class TestSolution(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(solution.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("dvdf"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("tmmzuxt"), 5)
if __name__ == '__main__':
    unittest.main()