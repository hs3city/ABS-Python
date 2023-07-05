import unittest

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest_prefix = ""
        j = 0
        for i in range(len(strs)):
            if i >= len(strs) - 1:
                break
            len_first = len(strs[i])
            len_second = len(strs[i+1])
            min_len = min(len_first, len_second)
            while j < min_len:
                if strs[i][j] == strs[i+1][j]:
                    longest_prefix += strs[i][j]
                    j += 1
                else:
                    break
        return longest_prefix


class TestCommonPrefix(unittest.TestCase):
    def test_two_different_words(self):
        x = ['flower', 'potato']

        result = Solution().longestCommonPrefix(x)

        assert result == ""

    def test_two_similar_words(self):
        x = ['flower', 'flour']

        result = Solution().longestCommonPrefix(x)

        self.assertEquals('flo', result)
