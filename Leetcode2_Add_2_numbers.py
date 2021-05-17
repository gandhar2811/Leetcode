curr = dummy = ListNode(0)
carry = 0
while l1 or l2:
    v1 = l1.val if l1 else 0
    v2 = l2.val if l2 else 0
    v3 = v1+v2+carry
    carry = v3//10
    v3 = v3%10
    curr.next = ListNode(v3)
    curr = curr.next
    l1 = l1.next if l1 else None 
    l2 = l2.next if l2 else None
return dummy.next
            
