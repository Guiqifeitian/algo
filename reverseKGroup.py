# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        temp = self.jump(head,k)
        # 如果节点数不足k个，则不用翻转，直接返回
        if not temp:
            return head
        # 使用递归，从后向前计算
        temp.next = self.reverseKGroup(temp.next,k)
        n =0
        # k个节点的翻转，注意第一个节点翻转时要指向下一段的开头
        while n< k -1:
            j = head.next
            if n == 0:
                head.next = temp.next
            else:
                head.next = temp
            temp = head
            head = j
            n += 1
        # k == 2的时候直接使用如下替换上面的while
        #head.next = temp.next
        #temp.next = head
        head.next = temp
        # 返回翻转后的起始节点
        return head
        
    def jump(self,head,k):
        # 返回从head向后走k-1个节点后的节点
        for i in range(k-1):
            if not head:
                return False
            else:
                head = head.next
        return head
