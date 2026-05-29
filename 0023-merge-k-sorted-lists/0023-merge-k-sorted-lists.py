class Solution:
    def mergeKLists(self, lists):

        values = []

        for linked_list in lists:

            while linked_list:
                values.append(linked_list.val)
                linked_list = linked_list.next

        if not values:
            return None

        values.sort()

        dummy = ListNode(0)
        current = dummy

        for value in values:
            current.next = ListNode(value)
            current = current.next

        return dummy.next