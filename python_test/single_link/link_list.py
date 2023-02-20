# https://juejin.cn/post/6992585857311965221
from node import Node, single_link, get_link, length


def reverse_recurse(node):
    """递归反转"""
    if node is None or node.next is None:
        return node
    res = reverse_recurse(node.next)
    node.next.next = node
    node.next = None
    return res


def reverse_iter(node):
    """迭代反转"""
    if node is None or node.next is None:
        return node
    pre = None
    while node:
        tmp = node.next
        node.next = pre
        pre = node
        node = tmp
    return pre


# 归并排序
def get_mid(node: Node):
    """找到链表中间节点"""
    if node is None or node.next is None:
        return node
    slow = node
    fast = node.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_sort(node: Node):
    """归并排序"""
    if node is None or node.next is None:
        return node
    mid = get_mid(node)
    right = mid.next
    mid.next = None
    left = merge_sort(node)
    right = merge_sort(right)
    return link_sort(left, right)


def link_sort(left: Node, right: Node):
    """合并两个有序链表"""
    if left is None:
        return right
    if right is None:
        return left
    if left.data < right.data:
        left.next = link_sort(left.next, right)
        return left
    else:
        right.next = link_sort(left, right.next)
        return right


def link_sort_(left: Node, right: Node):
    """合并两个有序链表"""
    cur = Node(0)
    head = cur
    while left != None and right != None:
        if left.data < right.data:
            cur.next = Node(left.data)
            cur = cur.next
            left = left.next
        else:
            cur.next = Node(right.data)
            cur = cur.next
            right = right.next
    if left != None:
        cur.next = left
    if right != None:
        cur.next = right
    res = head.next
    head.next = None
    return res


# 递归反转
a = single_link([99, 1, 34, 2, 6, 1, 35, 657, 5, 3, 8, 7])
print(f">>> 链表: {a} 长度: {length(a)}")
b = reverse_recurse(a)
print(f">>> 反转后的链表: {get_link(b)}")

# 迭代反转
a = single_link([99, 1, 34, 2, 6, 1, 35, 657, 5, 3, 8, 7])
c = reverse_iter(a)
print(f">>> 反转后的链表: {get_link(c)}, 长度: {length(c)}")


# 归并排序
a = single_link([3, 8, 1, 5, 2])
d = merge_sort(a)
print(f">>> 排序后的链表: {get_link(d)}, 长度: {length(d)}")
