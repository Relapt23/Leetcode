# You are given the head of a linked list, which contains a series of integers separated by 0's.
#  The beginning and end of the linked list will have Node.val == 0.

# For every two consecutive 0's,
#  merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes.
#  The modified list should not contain any 0's.

# Return the head of the modified linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self,head: Optional[ListNode]):
        node = ListNode(head)
        array =[]
        print(node)
        if self.val == 0:
            array.append(self.head)
            print(array)
        # data = head
        # sum = 0
        # array = []
        # ans = []
        # for i in data:
        #     if i == 0 and sum !=0:
        #         ans.append(sum)
        #         sum = 0
        #         continue
        #     if i != 0:
        #         sum += i
        # return ans

print(Solution.mergeNodes(self=ListNode, head=[0,1,0,3,0,2,2,0]))