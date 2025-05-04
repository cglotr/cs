/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode) {
	var reorder func(*ListNode, *ListNode) *ListNode

	reorder = func(root *ListNode, node *ListNode) *ListNode {
		if node == nil {
			return root
		}

		root_new := reorder(root, node.Next)

		if root_new == nil {
			return nil
		}

		if root_new == node || root_new.Next == node {
            node.Next = nil
            
			return nil
		} else {
			tmp := root_new.Next
			root_new.Next = node
			node.Next = tmp

			return tmp
		}
	}

	reorder(head, head.Next)
}
