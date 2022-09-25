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
        upper = 0

        while l1 and l2:
            print(l1.val, l2.val)
            s = l1.val + l2.val + upper
            if s < 10:
                sum_list.val = s
            else:
                sum_list.val = s - 10
                upper = 1


            l1 = l1.next
            l2 = l2.next

        return sum_list


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3, ListNode(5))))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    sol = Solution()
    print(sol.addTwoNumbers(l1, l2))



