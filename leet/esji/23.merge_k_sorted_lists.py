from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass

    def print_list_node(self, nodes):
        while nodes is not None:
            print(f"{nodes.val}", end="-")
            nodes = nodes.next


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    ins = Solution()

    ins.print_list_node(list1)