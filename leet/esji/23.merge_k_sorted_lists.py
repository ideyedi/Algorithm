from typing import List
from typing import Optional

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        head = point = ListNode(0)

        # 모든 링크드 리스트를 하나의 리스트로 통합
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next

        # Python Sorted O(nlogn)
        # 정렬된 리스트를 이용하여 새로운 linked list를 만든다.
        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next

        return head.next

    def print_list_node(self, nodes):
        while nodes is not None:
            print(f"{nodes.val}", end="-")
            nodes = nodes.next
        print("")


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))

    lists = [list1, list2, list3]
    ins = Solution()

    #ret = ins.mergeKLists(lists)
    ret = ins.merge_k_lists(lists)
    ins.print_list_node(ret)
    #ins.print_list_node(ret)
    #ins.print_list_node(list1)