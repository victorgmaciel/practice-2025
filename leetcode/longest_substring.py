"""Leetcode #3"""

string_one = "abcabcbb"
string_two = "bbbbb"
string_three = "pwwkew"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # creating a map to track characters
        # i.e. {}
        longest_substring = {}

        for characters in s:
            print(characters)
            if characters not in longest_substring:
                longest_substring



solution = Solution()

solution.lengthOfLongestSubstring(string_one)
