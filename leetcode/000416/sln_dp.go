func canPartition(nums []int) bool {
	n := len(nums)
	total := 0

	for _, num := range nums {
		total += num
	}

	if total%2 != 0 {
		return false
	}

	target := total / 2

	dp := make([]bool, target+1)
	dp[0] = true

	for i := 1; i < n+1; i++ {
		num := nums[i-1]

		for t := target; t >= num; t-- {
			dp[t] = dp[t] || dp[t-num]
		}
	}

	return dp[target]
}
