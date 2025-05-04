class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pool = set()

        for num in nums:
            pool.add(num)

        seen = set()
        ans = 0

        for num in nums:
            if num in seen:
                continue
            
            l = num
            r = num + 1

            while l in pool:
                seen.add(l)
                l -= 1

            while r in pool:
                seen.add(r)
                r += 1

            sz = r - l - 1
            ans = max(ans, sz)

        return ans
