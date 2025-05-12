func numDistinct(s string, t string) int {
	s_sz := len(s)
	t_sz := len(t)

	dp := [][]int{}

	for i := range s_sz + 1 {
		dp = append(dp, []int{})

		for _ = range t_sz + 1 {
			dp[i] = append(dp[i], 0)
		}
	}

	for i := range s_sz + 1 {
		dp[i][0] = 1
	}

	for i := 1; i < s_sz+1; i++ {
		s_ch := s[i-1]

		for j := 1; j < t_sz+1; j++ {
			dp[i][j] += dp[i-1][j]

			t_ch := t[j-1]

			if t_ch == s_ch {
				dp[i][j] += dp[i-1][j-1]
			}
		}
	}

	return dp[s_sz][t_sz]
}
