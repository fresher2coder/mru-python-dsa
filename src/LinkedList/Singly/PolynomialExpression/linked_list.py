from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, coef, expo):
        """Inserts a new node with the given coefficient and exponent at the end."""
        new_node = Node(coef, expo)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def traversal(self):
        """Traverses the linked list and prints the polynomial."""
        current = self.head
        if not current:
            print("List is empty")
            return

        result = []
        while current:
            term = f"{current.coef}"
            if current.expo != 0:
                term += f"x^{current.expo}"
            result.append(term)
            current = current.next

        print(" + ".join(result))

    def add(self, other):
        """Adds two polynomials represented as linked lists."""
        ptr1 = self.head
        ptr2 = other.head
        result = LinkedList()

        while ptr1 and ptr2:
            if ptr1.expo == ptr2.expo:
                result.insert_at_end(ptr1.coef + ptr2.coef, ptr1.expo)
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            elif ptr1.expo > ptr2.expo:
                result.insert_at_end(ptr1.coef, ptr1.expo)
                ptr1 = ptr1.next
            else:
                result.insert_at_end(ptr2.coef, ptr2.expo)
                ptr2 = ptr2.next

        # Add remaining nodes
        while ptr1:
            result.insert_at_end(ptr1.coef, ptr1.expo)
            ptr1 = ptr1.next

        while ptr2:
            result.insert_at_end(ptr2.coef, ptr2.expo)
            ptr2 = ptr2.next
        return result


