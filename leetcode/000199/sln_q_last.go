/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rightSideView(root *TreeNode) []int {
	ans := []int{}
	q := []*TreeNode{}
	if root != nil {
		q = append(q, root)
	}

	for len(q) > 0 {
		ans = append(ans, q[len(q)-1].Val)
		q_new := []*TreeNode{}

		for _, node := range q {
			if node.Left != nil {
				q_new = append(q_new, node.Left)
			}
			if node.Right != nil {
				q_new = append(q_new, node.Right)
			}
		}

		q = q_new
	}

	return ans
}
