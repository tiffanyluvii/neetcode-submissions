# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        fast = head
        slow = dummy

        for _ in range(n - 1):
            fast = fast.next

        while fast and fast.next:
            print("Fast", fast.val)
            print("Slow", slow.val)
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
         
        return dummy.next
        