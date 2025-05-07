/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func deleteNode(root *TreeNode, key int) *TreeNode {
	if root == nil {
		return nil
	}

	if key < root.Val {
		root.Left = deleteNode(root.Left, key)
	} else if key > root.Val {
		root.Right = deleteNode(root.Right, key)
	} else {
		if root.Left != nil {
			root.Val = getRightMostLeaf(root.Left).Val

			root.Left = deleteNode(root.Left, root.Val)
		} else if root.Right != nil {
			return root.Right
		} else {
			return nil
		}
	}

	return root
}

func getRightMostLeaf(node *TreeNode) *TreeNode {
	if node == nil {
		return nil
	}

	curr := node

	for curr.Right != nil {
		curr = curr.Right
	}

	return curr
}
