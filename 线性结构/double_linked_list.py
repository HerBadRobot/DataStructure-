class Node(object):
    """创建一个结点类"""

    def __init__(self, data):
        self.data = data
        self.pre = None
        self.next = None


class CreateDoubleLinkedList(object):
    """创建一个创建双向链表的类"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """判断双向链表是否为空链表"""
        return self.head is None

    def length(self):
        """获取双向链表的长度"""
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def traversal(self):
        """遍历双向链表"""
        cur = self.head
        if self.is_empty():
            print("链表为空！")
            return
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def node_is_exist(self, data):
        """查找指定结点是否存在"""
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return True
            else:
                cur = cur.next
        return False

    def add_first(self, data):
        """在头部添加结点"""
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            # 新结点向后指向头结点
            node.next = self.head
            # 头结点向前指向新结点
            self.head.pre = node
            # 将头结点的称号给新结点
            self.head = node

    def add_last(self, data):
        """在尾部添加结点"""
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            # 指针移动到尾部
            while cur.next is not None:
                cur = cur.next
            # 尾结点的后继指针指向新结点
            cur.next = node
            # 新结点的前驱指针指向尾结点
            node.pre = cur

    def insert_node(self, index, data):
        """在指定位置添加结点"""
        if index < 0 or index > self.length():
            print("结点位置错误！")
            return False
        elif index == 0:
            self.add_first(data)
        elif index == self.length():
            self.add_last(data)
        else:
            node = Node(data)
            cur = self.head
            pres = None
            count = 0
            # 移动到要添加的位置
            while count < index:
                pres = cur
                cur = cur.next
                count += 1
            # 新结点和它前面的结点互指
            pres.next = node
            node.pre = pres
            # 新结点和它后面的结点互指
            node.next = cur
            cur.pre = node

    def remove_node(self, data):
        """删除指定结点"""
        if self.is_empty():
            print("删除失败，链表为空！")
            return False
        elif data == self.head.data:
            self.head.next.pre = None
            self.head = self.head.next
        else:
            cur = self.head
            # 移动到要删除结点的位置
            while cur.data != data:
                cur = cur.next
            # 当前结点的后继结点为空，说明是尾结点
            if cur.next is None:
                cur.pre.next = None
                cur.pre = None
            else:
                cur.pre.next = cur.next
                cur.next.pre = cur.pre

    def reverse_traversal(self):
        """反向遍历双向链表"""
        if self.is_empty():
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        while cur is not None:
            print(cur.data)
            cur = cur.pre


if __name__ == '__main__':
    lists = CreateDoubleLinkedList()
    lists.add_last(3)
    lists.add_first(2)
    lists.add_first(1)
    lists.add_last(5)
    lists.insert_node(3, 4)
    lists.traversal()
    print("链表是否为空：", lists.is_empty())
    print("获取链表长度：", lists.length())
    print("改结点是否存在：", lists.node_is_exist(2))
    lists.remove_node(1)
    lists.remove_node(5)
    print("删除结点之后的遍历：")
    lists.traversal()
