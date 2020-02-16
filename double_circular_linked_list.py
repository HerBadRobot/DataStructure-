class Node(object):
    """结点类"""

    def __init__(self, data):
        self.data = data
        self.pre = None
        self.next = None


class CreateDoubleCircularLinkedList(object):
    """创建双向循环链表"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """判断双向循环链表是否为空"""

        return self.head is None

    def length(self):
        """获取双向循环链表的长度"""

        cur = self.head
        count = 0
        if self.is_empty():
            return 0
        while cur is not None:
            count += 1
            if cur.next == self.head:
                break
            else:
                cur = cur.next
        return count

    def traversal(self):
        """遍历双向循环链表"""

        if self.is_empty():
            print("链表为空")
            return
        cur = self.head
        while cur is not None:
            print(cur.data)
            if cur.next == self.head:
                break
            else:
                cur = cur.next

    def search_node(self, data):
        """查找指定结点是否存在"""
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return True
            # 如果已经查到尾部，则查找结束
            elif cur.next == self.head:
                return False
            else:
                cur = cur.next
        return False

    def set_empty(self):
        """将双向循环链表置空"""
        while self.is_empty() is False:
            self.remove_last()

    def add_first(self, data):
        """在头部添加结点"""

        node = Node(data)
        cur = self.head
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            while cur.next != self.head:
                cur = cur.next
            # 尾结点和新结点互指
            cur.next = node
            node.pre = cur
            # 新结点和头结点互指
            node.next = self.head
            self.head.pre = node
            # 将头指针给新结点
            self.head = node

    def add_last(self, data):
        """在尾部添加结点"""

        node = Node(data)
        cur = self.head
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            while cur.next != self.head:
                cur = cur.next
            # 连接尾部结点和新结点
            cur.next = node
            node.pre = cur
            # 连接新结点和头结点
            node.next = self.head
            self.head.pre = node

    def insert_node(self, index, data):
        """"在指定位置添加结点"""

        node = Node(data)
        if index < 0 or index > self.length():
            return False
        elif index == 0:
            self.add_first(data)
        elif index == self.length():
            self.add_last(data)
        else:
            cur = self.head
            pres = None
            count = 0
            # 指针移动到要添加的位置
            while count < index:
                pres = cur
                cur = cur.next
                count += 1
            # 连接前驱结点和新结点
            cur.pre.next = node
            node.pre = cur.pre
            # 连接后继结点和新结点
            node.next = cur
            cur.pre = node

    def remove_first(self):
        """删除头结点"""

        cur = self.head
        if self.is_empty():
            return False
        # 如果只有头结点一个
        elif self.head.next is self.head:
            self.head = None
            return True

        while cur.next != self.head:
            cur = cur.next
        # 连接尾结点和新的头结点
        cur.next = self.head.next
        self.head.next.pre = cur
        # 将头指针给新的头结点
        self.head = self.head.next

    def remove_last(self):
        """删除尾结点"""

        cur = self.head
        if self.is_empty():
            return False
        # 如果只有头结点一个
        elif self.head.next is self.head:
            self.head = None
            return True

        while cur.next != self.head:
            cur = cur.next
        # 连接新的尾结点和头结点
        cur.pre.next = self.head
        self.head.pre = cur.pre

    def remove_node(self, data):
        """删除指定结点"""

        cur = self.head
        if data == self.head.data:
            self.remove_first()
        else:
            while cur.data != data:
                cur = cur.next
            # 如果是尾结点
            if cur.next == self.head:
                self.remove_last()
            else:
                # 连接指定结点的前驱结点和后继结点
                cur.pre.next = cur.next
                cur.next.pre = cur.pre


if __name__ == '__main__':
    lists = CreateDoubleCircularLinkedList()
    lists.add_first(2)
    lists.add_first(1)
    lists.add_last(4)
    lists.insert_node(2, 3)
    print("是否为空：", lists.is_empty())
    print("获取长度：", lists.length())
    print("当前结点是否存在：", lists.search_node(2))
    lists.traversal()
    lists.remove_node(3)
    print("删除之后遍历")
    lists.traversal()
    lists.set_empty()
    print("置空之后的遍历")
    lists.traversal()
