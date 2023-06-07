"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def hasCycle(self, head:ListNode) -> bool:
        
        slow, fast = head, head        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow: return True            
        return False
    
    
# Create an instance of the Solution class
solution = Solution()
# Create the linked list with cycle (example assuming ListNode class exists)
head = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # This creates a cycle

# Call the hasCycle method on the solution instance and print the return value
print(solution.hasCycle(head))