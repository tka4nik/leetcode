# https://leetcode.com/problems/linked-list-cycle/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head):
    slow = fast = head
    while slow.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False



def print_list(head):
    el = head
    while el.next is not None:
        el = el.next
        print(el.val)


if __name__ == '__main__':
    ll = list(map(int, input().split()))

    head = ListNode(ll[0])
    link = ListNode()
    head.next = link
    for i in ll[1:]:
        link.next = ListNode(i)
        link = link.next
    print_list(head)
    print_list(solution(head))
