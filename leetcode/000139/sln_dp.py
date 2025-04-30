class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = set()
        dp.add('')

        for i in range(n):
            for word in wordDict:
                if (i + 1) >= len(word):
                    prev = s[:i + 1 - len(word)]
                    if prev in dp:
                        dp.add(prev + word)

        return s in dp
