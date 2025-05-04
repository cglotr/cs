import "slices"

func threeSum(nums []int) [][]int {
	slices.SortFunc(nums, func(a, b int) int {
		return a - b
	})

	n := len(nums)
	ans := [][]int{}

	for i := 0; i < n; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
        
		l := i + 1
		r := n - 1
		want := -nums[i]

		for l < r {
			have := nums[l] + nums[r]

			if have == want {
				ans = append(ans, []int{nums[i], nums[l], nums[r]})

				l += 1

				for l < r && nums[l] == nums[l-1] {
					l += 1
				}
			} else if have > want {
				r -= 1
			} else {
				l += 1
			}
		}
	}

	return ans
}
