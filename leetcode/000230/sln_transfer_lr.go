/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthSmallest(root *TreeNode, k int) int {
	ans := -1

	var dfs func(*TreeNode, int) int
	dfs = func(node *TreeNode, size int) int {
		if node == nil {
			return size
		}

		l := dfs(node.Left, size)

		if 1+l == k {
			ans = node.Val
		}

		r := dfs(node.Right, 1+l)

		return r
	}

	dfs(root, 0)

	return ans
}
