from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        pass

    def __reversed(self):
        """
        Private method
        :return: reversed linked list
        """
        return 0

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        :param head: input linked list, range 0 <= head.val <= 1000
        :param k: Range 1 <= k <= n <= 5000
            n: The number of nodes in the list
        :return: reversed linked list
        """
        if k == 1 or not head:
            return head

        swap_node = ListNode(-1, head)

        prev = swap_node
        curr = swap_node
        next_node = swap_node
        count = 0

        # Linked List counting
        # Time Complexity: O(n)
        while curr:
            curr = curr.next
            count += 1

        count -= 1
        # next node가 NoneType일 경우 순회를 종료
        while next_node:
            curr = prev.next
            next_node = curr.next

            to_loop = count > k and k or count - 1

            for _ in range(1, to_loop):
                curr.next = next_node.next
                next_node.next = prev.next

                prev.next = next_node
                next_node = curr.next

            prev = curr
            count -= k

        return swap_node.next


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
    linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    obj = Solution()

    print_linked_list(linked_list)
    linked_list = obj.reverseKGroup(linked_list, 3)
    print_linked_list(linked_list)
