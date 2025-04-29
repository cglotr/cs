class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        def bs(l, r):
            while l <= r:
                m = l + (r - l)//2
                if nums[m] == target:
                    return m
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            return -1

        def find(l, r):
            if l > r:
                return -1
            m = l + (r - l)//2
            if nums[m] == target:
                return m

            # left sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    return bs(l, m - 1)
                else:
                    return find(m + 1, r)
            # right sorted
            else:
                if nums[m] < target <= nums[r]:
                    return bs(m + 1, r)
                else:
                    return find(l, m - 1)

        return find(0, len(nums) - 1)
