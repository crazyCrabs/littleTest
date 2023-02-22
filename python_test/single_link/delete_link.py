# 删除链表倒数的第n个节点
# https://blog.csdn.net/qq_45556599/article/details/104765826
# https://xiulian.blog.csdn.net/article/details/113098149?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-1-113098149-blog-104765826.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-1-113098149-blog-104765826.pc_relevant_default&utm_relevant_index=1

from node import *


# 遍历链表删除
def removeNthFromEnd(head: Node, n: int) -> Node:
    "遍历链表删除"
    dummy = Node(0)
    dummy.next = head
    length = 0
    first = head
    while first != None:
        length += 1
        first = first.next
    length -= n
    first = dummy
    while length > 0:
        length -= 1
        first = first.next
    first.next = first.next.next
    return dummy.next

    # 需要注意n==length的情况，此时需要删除头节点
    # node_length = length(head)
    # if node_length == n:
    #     return head.next
    # cur = head
    # for _ in range(node_length - n - 1):
    #     cur = cur.next
    # cur.next = cur.next.next
    # return head

# 利用栈
def removeNthFromEnd_1(head: Node, n: int) -> Node:
    "利用栈 加个头节点就不用判断删除头节点的情况了"
    dummy = Node(0)
    dummy.next = head
    stack = []
    cur = dummy
    while cur != None:
        stack.append(cur)
        cur = cur.next
    for _ in range(n):
        stack.pop()
    top = stack.pop()
    top.next = top.next.next
    return dummy.next


# 快慢指针
def removeNthFromEnd_2(head: Node, n: int) -> Node:
    "快慢指针"
    dummy = Node(0)
    dummy.next = head
    first = dummy
    second = dummy
    for _ in range(n + 1):
        first = first.next
    while first != None:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next


if __name__ == "__main__":
    head = single_link([1, 2, 3, 4, 5, 6])
    # print(get_link(removeNthFromEnd_2(head, 5)))

    # 找到链表的中间节点
    # https://blog.csdn.net/unseven/article/details/122971089
    def get_mid(head: Node) -> Node:
        "快慢指针"
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    print(get_mid(head))
