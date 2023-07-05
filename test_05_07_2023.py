import unittest

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest_prefix = ""
        for i in range(len(strs)):
            if strs[i][0] == strs[i+1][0]:
                longest_prefix += strs[i][0]
            else:
                break
        return longest_prefix


class TestCommonPrefix(unittest.TestCase):
    def test_two_different_words(self):
        x = ['flower', 'potato', 'flour']

        result = Solution().longestCommonPrefix(x)

        assert result == ""
