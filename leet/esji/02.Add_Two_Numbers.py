#! python
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        pass

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_list = ListNode()
        curr = sum_list
        upper = 0

        # and 연산이 아니고 or로 처리해야하며, upper 값도 조건에 추가
        while l1 or l2 or upper:
            # 10 이상으로 합이 넘어 온 경우 먼저 처리해야함
            # l1, l2를 따로 구분해서 처리해야하는 구나..
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            column_sum = l1_val + l2_val + upper
            # 이런식으로 구현하는게 더 깔끔한듯
            upper = column_sum // 10
            new_node = ListNode(column_sum % 10)
            curr.next = new_node
            curr = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return sum_list.next


def print_linked_list(nodes):
    """
    :param nodes: 입력된 링크드 리스트 내용을 확인을 위한 출력 함수
    :return: 리스트 값이 없을 때까지 해당 노드의 값을 출력
    """
    while nodes is not None:
        print(f'{nodes.val}', end=",")
        nodes = nodes.next
    print('\n'+'-'*20)


if __name__ == "__main__":
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    sol = Solution()
    #print(sol.addTwoNumbers(l1, l2))
    print_linked_list(sol.addTwoNumbers(l1, l2))



