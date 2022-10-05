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

        while l1 and l2:
            # 10 이상으로 합이 넘어 온 경우 먼저 처리해야함
            s = l1.val + l2.val + upper 
            upper = s // 10
            curr.val = s % 10
            
            if l1.next or l2.next:
                curr.next = ListNode()
                curr = curr.next
            
            l1 = l1.next
            l2 = l2.next 

        return sum_list


def print_linked_list(nodes):
    """
    :param nodes: 입력된 링크드 리스트 내용을 확인을 위한 출력 함수
    :return: 리스트 값이 없을 때까지 해당 노드의 값을 출력
    """
    while nodes is not None:
        print(f'{nodes.val}', end="->")
        nodes = nodes.next
    print('\n'+'-'*20)


if __name__ == "__main__":
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    sol = Solution()
    #print(sol.addTwoNumbers(l1, l2))
    print_linked_list(sol.addTwoNumbers(l1, l2))



