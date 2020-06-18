# input
# v1 v2 ... vn (value of each node)
# p (pos: which represents the position(index) in the linked list where tail connects to)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # def addNode(self, x):
    #     self.next.val = x
    #     self.next.next = None

class Solution:
    # this method is the answer
    def hasCycle(self, head: ListNode) -> bool:
        """
        type head: ListNode
        return type: bool
        """

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# not related to the answer
# main function for checking correctness by myself
if __name__ == '__main__':
    l = list(map(int, input().split()))
    head = ln = ListNode(l[0])
    for i in range(1, len(l)):
        ln.next = ListNode(l[i])
        ln = ln.next
    
    pos = int(input())
    if pos != -1:
        to = head
        for i in range(pos):
            to = to.next
        ln.next = to

    s = Solution()
    if s.hasCycle(head):
        print('true')
    else:
        print('false')



