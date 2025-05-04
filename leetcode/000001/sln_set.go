func twoSum(nums []int, target int) []int {
	seen := map[int]int{}

	for i, v := range nums {
		want := target - v

		if _, ok := seen[want]; ok {
			return []int{seen[want], i}
		}

		seen[v] = i
	}

	return []int{}
}
