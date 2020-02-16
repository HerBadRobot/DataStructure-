class Node(object):
    """创建单个结点类"""
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList(object):
    """创建一个单链表"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def length(self):
        """获取链表的长度"""
        
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def traversal(self):
        """遍历整个链表"""
        
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def search_node_is_exist(self, data):
        """查找指定结点是否存在"""
        
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return True
            else:
                cur = cur.next
        return False

    def add_fist(self, data):
        """在链表的头部添加元素"""
        
        node = Node(data)
        node.next = self.head
        self.head = node

    def add_last(self, data):
        """在链表的尾部添加元素"""
        
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert_node(self, index, data):
        """在指定位置添加元素"""
        
        node = Node(data)
        if index < 0 or index > self.length():
            return False
        elif index == 0:
            self.add_fist()
        else:
            cur = self.head
            count = 0
            while count < index - 1:
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    def remove_node(self, data):
        """删除指定结点"""
        
        cur = self.head  # 指针指向的结点
        pre = None  # 指针指向结点的前一个
        if self.head == data:
            self.head.next = self.head
        else:
            while cur.data is not data:
                pre = cur
                cur = cur.next
            pre.next = cur.next


if __name__ == '__main__':
    lists = SingleLinkedList()
    lists.add_fist(2)
    lists.add_fist(1)
    lists.add_last(4)
    lists.insert_node(2, 3)
    lists.traversal()
    print(lists.is_empty())
    print(lists.length())
    lists.insert_node(4, 5)
    lists.remove_node(4)
    print(lists.search_node_is_exist(3))
    lists.traversal()
