class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
  first = ListNode
  result = first

  while(True):
    if(list1 == None):
      result.next = list2
      break
    if (list2 == None):
      result.next = list1
      break

    if list1.val <= list2.val:
      result.next = list1
      result = result.next
      list1 = list1.next
      continue
    if list1.val > list2.val:
      result.next = list2
      result = result.next
      list2 = list2.next
      continue

  return first.next



list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

test = mergeTwoLists(list1, list2)
print(test)