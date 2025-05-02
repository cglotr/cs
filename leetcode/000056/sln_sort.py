class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        A = []

        for s, e in intervals:
            A.append((s, e))

        A.sort()

        ans = []

        for s, e in A:
            if len(ans) > 0 and s <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], e)
            else:
                ans.append([s, e])

        return ans
