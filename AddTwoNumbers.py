import unittest

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        next = l1.next
        num1 = l1.val
        i = 1
        while next is not None:
            num1 += next.val * (10 ** i)
            next = next.next
            i+=1

        next = l2.next
        num2 = l2.val
        i = 1
        while next is not None:
            num2 += next.val * (10 ** i)
            next = next.next
            i+=1
        
        tot = num1 + num2
        node0 = None
        for digit in [int(i) for i in str(tot)]:
            node1 = ListNode(digit, node0)
            node0 = node1
        
        return node0



class TestAddTwoNumbers(unittest.TestCase):
    def test_addTwoNumbers(self):
        node_10 = ListNode(3, None)
        node_11 = ListNode(4, node_10)        
        node_12 = ListNode(2, node_11)

        
        node_20 = ListNode(4, None)
        node_21 = ListNode(6, node_20)        
        node_22 = ListNode(5, node_21)

        solution = Solution()
        solution.addTwoNumbers(node_12, node_22)

if __name__ == '__main__':
    unittest.main()