#1836
from collections import defaultdict

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        def collect(node):
            cont = defaultdict(int)        
            while node:
                cont[node.val] += 1
                node = node.next
            return cont
        
        points = {x for x,y in collect(head).items() if y>1}
        
        node = head
        prev = None
        
        while node:
            if node.val in points:
                # we need to remove the node
                if prev == None:
                    # it is the head node
                    head = node.next
                    node = node.next
                    # loop back around
                    continue
                    
                elif not node.next:
                    # it is the last node
                    prev.next = None
                    break
                    
                else:
                    prev.next = node.next
                    # we're somewhere in the middle
                    node = node.next
                    continue
            prev = node
            node = node.next
            
        return head
            