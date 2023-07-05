import unittest


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest_prefix = strs[0]
        for i in range(1, len(strs)):
            if i >= len(strs):
                break
            len_prefix = len(longest_prefix)
            len_second = len(strs[i])
            min_len = min(len_prefix, len_second)
            for j in range(min_len):
                if strs[i][j] == longest_prefix[j]:
                    continue
                else:
                    longest_prefix = strs[i][:j]
                    break
        return longest_prefix


class TestCommonPrefix(unittest.TestCase):
    def test_two_different_words(self):
        x = ['flower', 'potato']

        result = Solution().longestCommonPrefix(x)

        self.assertEquals(result, "")

    def test_two_similar_words(self):
        x = ['flower', 'flour']

        result = Solution().longestCommonPrefix(x)

        self.assertEquals('flo', result)

    def test_second_word_completely_different_than_first(self):
        x = ['flower', 'potato', 'bakery']

        result = Solution().longestCommonPrefix(x)

        self.assertEquals('', result)

    def test_one_empty_word(self):
        x = [""]

        result = Solution().longestCommonPrefix(x)

        self.assertEquals('', result)
    def test_first_longer_than_latter(self):
        x = ["ab", "a"]
        result = Solution().longestCommonPrefix(x)

        self.assertEquals('', result)
# TODO:
"""
1. niewydajność dla 1 testu?
2. więcej niz 2 wyrazy
"""

x = ['flower', 'potato']

result = Solution().longestCommonPrefix(x)