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
	dp := [][]bool{}

	for i := 0; i < n+1; i++ {
		dp = append(dp, []bool{})

		for t := 0; t < target+1; t++ {
			dp[i] = append(dp[i], false)
		}
	}

	dp[0][0] = true

	for i := 1; i < n+1; i++ {
		num := nums[i-1]

		for t := target; t > 0; t-- {
			if t >= num {
				dp[i][t] = dp[i-1][t] || dp[i-1][t-num]
			} else {
				dp[i][t] = dp[i-1][t]
			}
		}
	}

	return dp[n][target]
}
