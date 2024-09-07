
# https://leetcode.com/problems/reverse-linked-list/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head):
    prev, curr = None, head

    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev


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
