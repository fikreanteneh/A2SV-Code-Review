# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        front = None
        back = head
        count = 0
        if head is None or head.next is None: return head #don't use one line 
        while back: 
            back = back.next
            count += 1
        k, count, back = k%count, 0, head   #don't use one line 
        if k == 0: return head   #don't use one line and give space between codos to make it clear to see
        while back.next:
            back = back.next
            count+= 1
            if back.next is None and count < k: 
                back = head
                count += 1
            
            if k == count: front = head
            elif front: front = front.next
        back.next = head
        main = front.next
        front.next = None
        return main
    
    # it is good aproche but your code is a little bit mess try to make it clear 
    # and good naming i like it 
