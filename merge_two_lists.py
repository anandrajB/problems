from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        return dummy.next


solution = Solution()
find_mergers = solution.mergeTwoLists(
    list1=ListNode(1, ListNode(2, ListNode(4))),
    list2=ListNode(1, ListNode(3, ListNode(4))),
)


# using numpy

# def merge_list_1(list1, list2):
#     import numpy as np

#     return np.sort(np.concatenate((list1, list2)))


# using 2 pointers
def merge_list_2(list1, list2):
    final_list = []

    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            final_list.append(list1[i])
            i += 1
        else:
            final_list.append(list2[j])
            j += 1

    return final_list


list1 = [1, 2, 5, 6]
list2 = [2, 4, 5, 4]

print(merge_list_2(list1, list2))


# using basic sorted


sorted(list1 + list2)# time complexity O( m + n)
