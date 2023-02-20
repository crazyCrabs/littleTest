# 合并两个有序链表
# https://blog.csdn.net/z_feng12489/article/details/106105227


from node import *


def combine_link(head1, head2):
    "递归合并两个有序链表"
    if not head1:
        return head2
    if not head2:
        return head1
    if head1.data < head2.data:
        head1.next = combine_link(head1.next, head2)
        return head1
    else:
        head2.next = combine_link(head1, head2.next)
        return head2


def combine_link_(head1, head2):
    "迭代合并两个有序链表"
    cur = Node(0)
    head = cur
    while head1 != None and head2 != None:
        if head1.data < head2.data:
            cur.next = head1
            head1 = head1.next
        else:
            cur.next = head2
            head2 = head2.next
        cur = cur.next
    if head1 != None:
        cur.next = head1
    if head2 != None:
        cur.next = head2
    res = head.next
    head.next = None
    return res


if __name__ == "__main__":
    head1 = single_link([1, 3, 5, 7])
    head2 = single_link([2, 4, 6, 8])

    # link = combine_link(head1, head2)
    # print(get_link(link))

    print(get_link(combine_link_(head1, head2)))
