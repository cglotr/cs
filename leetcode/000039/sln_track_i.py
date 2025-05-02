class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []

        def comb(arr, t, i):
            if t <= 0:
                if t == 0:
                    self.ans.append(arr)
                return
            if i >= len(candidates):
                return

            comb(arr + [candidates[i]], t - candidates[i], i)
            comb(arr, t, i + 1)

        comb([], target, 0)

        return self.ans
