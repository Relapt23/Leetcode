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
    def mergeNodes(head: Optional[ListNode]):
        sum = 0
        array = []
        ans = []
        for head.val in head:
            if head.next == 0 and sum !=0:
                ans.append(sum)
                sum = 0
                continue
            if head.next != 0:
                sum += head.val
        return ans

print(Solution.mergeNodes(head=[0,1,0,3,0,2,2,0]))