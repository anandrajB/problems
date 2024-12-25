from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        has_odd = False

        for count in Counter(s).values():
            #  check for even first
            length += (count // 2) * 2
            if (count % 2) == 1:
                has_odd = True

        return length + (1 if has_odd else 0)


solution = Solution()
print(solution.longestPalindrome("abccccdd"))  # Output: 7
