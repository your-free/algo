import math
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def list_to_tree(self,sortlist):
		
		if(sortlist==None):
			return None
		if(len(sortlist)==0):
			return None
		if(len(sortlist)==1):

			root = TreeNode(sortlist[0])
			
			root.left = None
			root.right = None
			return root

		n = len(sortlist)
		cen = math.ceil(n/2)-1
		left_child = self.list_to_tree(sortlist[0:cen])
		
		right_child = self.list_to_tree(sortlist[cen+1:n])
		
		root = TreeNode(sortlist[cen])
		root.left =  left_child
		root.right = right_child		
		
		return root

	def sortedListToBST(self, head: ListNode): #-> TreeNode:
		arr = []
		node = head
		if(node==None):
			return None
		if(node.next==None):
			root = TreeNode(node.val)
			root.left = None
			root.right = None
			return root

		while(node.next!=None):
			arr.append(node.val)
			node = node.next
		arr.append(node.val)
		
		root = self.list_to_tree(arr)
		return root
