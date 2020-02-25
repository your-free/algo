# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# flatten in place with right child carrying the next node
class Solution:
	def flat_sub(self,node):
		head = None
		
		if(node==None):
			return node, node

		if(node.left==None and node.right==None):
			#print("leaf node:", node.val)
			head  = node
			last  = node
			return head, last
		
		left_head , left_last = self.flat_sub(node.left)	
		right_head , right_last = self.flat_sub(node.right)	
		
		if(left_head!=None):
		    node.right = left_head
		    left_last.right = right_head
		else:
			node.right=right_head
		
		if(right_last==None):
			last = left_last
		else:
			last = right_last
			
		node.left = None    
		return node, last


	def flatten(self, root):
	    """
	    Do not return anything, modify root in-place instead.
	    """

	    if(root == None):
	    	return
	    else:
	    	root,last= self.flat_sub(root)
        