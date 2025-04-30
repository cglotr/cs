class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        n = len(s)

        for sz in range(n, 0, -1):
            for i in range(n):
                j = i + sz - 1
                if j < n:
                    if pal(i, j):
                        return s[i:j + 1]

        return ''
