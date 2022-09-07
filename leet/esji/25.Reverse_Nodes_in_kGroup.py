from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        pass

    def reverseKGroupPhase1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
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

        return swap_node.next

    def reverseKGroup(self, head: ListNode, k: int) -> Optional[ListNode]:
        """
        :param head:
        :param k:
        :return:
        Reference solution
        """
        if k == 1 or not head:
            return head
        # 더미 노드 생성, 내가 했던 방식이랑 동일한 소스 인거 같은데
        #dummy = ListNode(0, None)
        #dummy.next = head
        dummy = ListNode(-1, head)
        start = dummy
        # Q: end의 사용처는 무엇인가
        end = head
        count = 0

        # 처음 Linked List의 count check loop가 없음
        # 아 count, k의 나머지를 이용해서 끝에 남는 부분을 걸러냈구나!
        # 나머지가 0일 경우 swap을 수행
        while end:
            count += 1
            if count % k == 0:
                start = self.__reverse(start, end.next)
                end = start.next
            else:
                end = end.next
        return dummy.next

    def __reverse(self, start, end):
        """
        :discription
        입력받은 리스트를 뒤집는 함수
        :param start:
        :param end:
        :return:
        """
        # swap 로직 자체는 차이가 없음..
        # 그래도 함수로 뺀게 더 나이스함
        prev, curr = start, start.next
        first = curr
        while curr != end:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        start.next = prev
        first.next = curr

        return first


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
