class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f"Node<{str(self.data)}>"


def single_link(data: list):
    head, cur = None, Node(None)
    for i, v in enumerate(data):
        if i == 0:
            head = Node(v)
            cur = head
        else:
            cur.next = Node(v)
            cur = cur.next
    return head


def get_link(node: Node):
    links = []
    while node != None:
        links.append(node.data)
        node = node.next
    return links


def length(node: Node):
    """链表长度"""
    count = 0
    while node:
        count += 1
        node = node.next
    return count
