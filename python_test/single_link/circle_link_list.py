# 判断链表中是否有环
# https://blog.csdn.net/weixin_41296050/article/details/108960332

from typing import Optional

from node import Node


def exists_circle1(node: Node) -> bool:
    """哈希表 判断链表中是否有环"""
    if node is None or node.next is None:
        return False
    nodes = set()
    while node:
        if node in nodes:
            return True
        nodes.add(node)
        node = node.next
    return False


def exists_circle2(node: Node) -> bool:
    "反转链表 判断链表中是否有环"
    if node is None or node.next is None:
        return False
    pre = None
    cur = node
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre == node


def exists_circle3(node: Node) -> bool:
    """快慢指针 判断链表中是否有环"""
    if node is None or node.next is None:
        return False
    slow = node
    fast = node.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def find_circle_entry(node: Node) -> Optional[Node]:
    """找到环的入口"""
    if node is None or node.next is None:
        return None
    slow, fast = node, node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    slow = node
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node3

    # 集合判断是否存在环
    # print(exists_circle1(node1))

    # 反转链表判断是否存在环 会破环链表
    # print(exists_circle2(node1))

    # 快慢指针判断是否存在环
    print(exists_circle3(node1))

    # 找到环的入口
    print(find_circle_entry(node1))
