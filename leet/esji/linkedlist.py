from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        pass

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        print(head.val)
        print(head.next)

    def print(self):
        pass


if __name__ == "__main__":
    linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(linked_list.val)
    print(linked_list.next)