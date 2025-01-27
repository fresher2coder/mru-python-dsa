class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None

        slow, fast = head, head

        # Detect the cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Cycle detected
                break
        else:
            # If no cycle, return None
            return None

        # Find the entry point of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  # Starting node of the cycle
