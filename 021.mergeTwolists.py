'''第21题：
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists/
'''
    # 定义一个单链表结点
class ListNode:
    # 定义一个单链表结点
    def __init__(self, val=0,next = None):
        self.val = val
        self.next = next
    #定义一个单链表
class LinkList:
    def __init__(self,val = 0,next = None):
        self.head = ListNode(val,next)

    def isEmpty(self):
        if self.head.next is None:
            return True
        return False

    def initlist(self,data_list):
        if (self.isEmpty() == True) & (len(data_list)==0):   #[1]理论上也是单链表
            return None
        else:
            self.head = ListNode(data_list[0])
            p = self.head

            for i in data_list[1:]:
                node = ListNode(i)
                p.next = node
                p = p.next
            return self.head

def getNodes(head_node):
    result = []
    while head_node is not None:
        result.append(head_node.val)
        head_node = head_node.next
    return result

class solution:
    def mergeTwoLists(self,s1:ListNode,s2:ListNode):
        if s1 is None:
            return s2
        elif s2 is None:
            return s1
        elif s1.val < s2.val:
            s1.next = self.mergeTwoLists(s1.next, s2)
            return s1
        else:
            s2.next = self.mergeTwoLists(s1, s2.next)
            return s2
#测试
a = [1]
b = [1,2,4]
s = LinkList()

s1 = s.initlist(a)
s2 = s.initlist(b)

print(getNodes(s1))
print(getNodes(s2))

s = solution()
print(getNodes(s.mergeTwoLists(s1,s2)))

