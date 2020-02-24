# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        node = head
        if(node==None):
            return node
        if(node.next==None):
       		return head
        n=1
        while(node.next!=None):
	       	node.next.prev = node
	       	node=node.next
	       	n+=1
        
        head.prev = node
        node.next = head
        if(k>n):
            k = k % n
        # node here is the end node	
        i = 1
        while(i<=k):
    	   	i+=1

       		node = node.prev
       		#print(node.val)
       	new_start = node.next	
       	node.next = None
       	head = new_start
        return head

arr = [1,2,3,4,5]

head = ListNode(arr[0])
node = head
for i in range(1,len(arr)):
	node.next = ListNode(arr[i])
	node = node.next
Solution().rotateRight(head,2)