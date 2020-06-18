# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        l = []
        now = head
        if now == None:
            return None
        next = head.next

        while now and next:
            if next in l:
                return next
            else:
                l.append(now)
                now = now.next
                next = next.next
        return None

    
    def detectCycle2(self, head):
        try:
            fast = head.next
            slow = head
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
        except:
            return None
        
        slow = slow.next
        while slow is not head:
            head = head.next
            slow = slow.next
        return head




