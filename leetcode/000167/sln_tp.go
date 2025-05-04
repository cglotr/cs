func twoSum(numbers []int, target int) []int {
	l := 0
	r := len(numbers) - 1

	for l < r {
		have := numbers[l] + numbers[r]

		if have == target {
			return []int{l + 1, r + 1}
		} else if have > target {
			r -= 1
		} else {
			l += 1
		}
	}

	return []int{}
}
