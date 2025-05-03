class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_cnt = collections.defaultdict(int)
        t_cnt = collections.defaultdict(int)

        for ch in t:
            t_cnt[ch] += 1

        l = 0
        ans = ''
        ans_ln = math.inf

        def is_good():
            for ch in t_cnt:
                if s_cnt[ch] < t_cnt[ch]:
                    return False

            return True

        def capture(r):
            nonlocal l
            nonlocal ans
            nonlocal ans_ln
            cand = s[l:r + 1]

            if len(cand) < ans_ln:
                ans = cand
                ans_ln = len(cand)

            if l <= r:
                s_cnt[s[l]] -= 1
                l += 1

        for r in range(len(s)):
            s_cnt[s[r]] += 1

            while is_good():
                capture(r)

        while is_good():
            capture(len(s) - 1)

        return ans
