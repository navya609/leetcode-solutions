class Solution:
    def rotateRight(self, head, k):

        if not head or not head.next or k == 0:
            return head

        # Find length and tail
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Reduce rotations
        k = k % length

        if k == 0:
            return head

        # Make circular
        tail.next = head

        # Find new tail
        steps = length - k - 1
        newTail = head

        for _ in range(steps):
            newTail = newTail.next

        # New head
        newHead = newTail.next

        # Break circle
        newTail.next = None

        return newHead