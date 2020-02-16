class Node(object):
    """创建一个结点类"""
    def __init__(self, data):
        self.data = data
        self.next = None

class create_circular_linked_list(object):
    """创建一个创建循环链表的类"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """判断循环链表是否为空"""
        return self.head is None

    def length(self):
        """获取循环链表的长度"""
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            # 如果当前结点的下一个结点是头结点，说明这个结点就是尾结点
            # 如果不是，就将指针向后移动一个
            if cur.next == self.head:
                break
            else:
                cur = cur.next
        return count

    def add_first(self, data):
        """在头部添加结点"""
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            # 将指针移动到尾部结点
            while cur.next is not self.head:
                cur = cur.next
            # 尾部结点指向新节点
            cur.next = node
            # 新结点指向原来的头结点
            node.next = self.head
            # 再将头结点的称号给新结点
            self.head = node

    def add_last(self, data):
        """在尾部添加结点"""
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            # 将指针移动到尾部
            while cur.next is not self.head:
                cur = cur.next
            # 尾部结点指向新结点
            cur.next = node
            # 新结点指向头结点
            node.next = self.head

    def insert_node(self, index, data):
        """在指定位置插入结点"""
        node = Node(data)
        if index < 0 or index > self.length():
            print("插入位置错误")
            return False
        elif index == 0:
            self.add_first(data)
        else:
            cur = self.head
            pre = None # pre为当前指针所指向结点的前一个结点
            count = 0
            # 将指针移动到要插入的位置
            while count < index:
                pre = cur
                cur = cur.next
                count += 1
            pre.next = node
            node.next = cur

    def remove_node(self, data):
        """删除指定结点"""
        if self.is_empty():
            return
        # 如果要删除的结点就是头结点
        elif data == self.head.data:
            # 如果链表只有一个头结点
            if self.head.next is self.head:
                self.head = None
            else:
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next
                cur.next = self.head.next
                self.head = self.head.next
        else:
            cur = self.head
            pre = None
            # 移动到要删除结点的位置
            while cur.data != data:
                # 如果没找到
                if cur.next == self.head:
                    return
                pre = cur
                cur = cur.next
            # 将要删除的结点的前驱结点指向后继结点，这样就跳过了中间的结点
            pre.next = cur.next

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self.head
        print(cur.data)
        while cur.next != self.head:
            cur = cur.next
            print(cur.data)

    def is_exist(self, data):
        """查找指定结点是否存在"""
        cur = self.head
        while cur is not None:
            # 找到所查结点
            if cur.data == data:
                return True
            # 已经查到尾部了
            elif cur.next == self.head:
                return False
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    lists = create_circular_linked_list()
    lists.add_last(2)
    lists.remove_node(2)
    print(lists.is_empty())
    lists.add_first(1)
    lists.add_first(0)
    lists.add_last(3)
    lists.insert_node(2, 8)
    lists.travel()
    print("链表长度:", lists.length())
    lists.remove_node(8)
    lists.travel()
    print(lists.is_exist(2))
