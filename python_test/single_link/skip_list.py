# https://zhuanlan.zhihu.com/p/54869087
import random


class ListNode:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = []

    def __repr__(self) -> str:
        return f'ListNode<data: {self.data}>'


class SkipList():
    _MAX_LEVEL = 4

    def __init__(self) -> None:
        self._level_count = 1
        self.head = ListNode()
        self.head.next = [None] * SkipList._MAX_LEVEL

    def insert(self, value):
        level = self._random_level()
        self._level_count = max(self._level_count, level)
        new_node = ListNode(value)
        new_node.next = [None] * level
        update = [self.head] * level

        p = self.head
        for i in range(level - 1, -1, -1):
            while p.next[i] and p.next[i].data < value:
                p = p.next[i]
            if p.next[i] and p.next[i].data == value:
                return False  # 已存在
            update[i] = p  # 记录每层的前驱节点

        for i in range(level):
            new_node.next[i] = update[i].next[i]  # 将新节点插入到每层的前驱节点后面
            update[i].next[i] = new_node  # 将每层的前驱节点的后继节点指向新节点
        return True

    def _random_level(self):
        level = 1
        while random.randint(0, 1) == 1 and level < self._MAX_LEVEL:
            level += 1
        return level

    def delete(self, value):
        update = [None] * self._level_count
        p = self.head
        for i in range(self._level_count - 1, -1, -1):
            while p.next[i] and p.next[i].data < value:
                p = p.next[i]
            update[i] = p

        if p.next[0] and p.next[0].data == value:
            for j in range(self._level_count - 1, -1, -1):
                if update[j].next[j] and update[j].next[j].data == value:
                    update[j].next[j] = update[j].next[j].next[j]
            return True
        else:
            return False

    def find(self, value):
        p = self.head
        for i in range(self._level_count - 1, -1, -1):
            while p.next[i] and p.next[i].data < value:
                p = p.next[i]
            if p.next[i] and p.next[i].data == value:
                return p.next[i]

    def find_range(self, begin_value, end_value):
        p = self.head
        begin = None
        for i in range(self._level_count - 1, -1, -1):
            while p.next[i] and p.next[i].data < begin_value:
                p = p.next[i]
            if p.next[i] and p.next[i].data >= begin_value:
                begin = p.next[i]
        if begin is None:
            return None
        result = []
        while begin and begin.data <= end_value:
            result.append(begin)
            begin = begin.next[0]
        return result

    def pprint(self):
        for i in range(self._level_count - 1, -1, -1):
            p = self.head
            format_str = f'level {i}: '
            while p:
                if p.data:
                    format_str += f'-> {p.data}'
                p = p.next[i]
            print(format_str)


if __name__ == "__main__":
    l = SkipList()

    for i in range(1, 12):
        l.insert(i)
    l.pprint()

    # 删除7
    if l.delete(7):
        print('delete 7 success')
    l.pprint()

    # 查找5
    node = l.find(5)
    print(f'find 5: {node}')

    # 查找区间[3, 8]
    for i in l.find_range(3, 8):
        print(i.data, end='->')
