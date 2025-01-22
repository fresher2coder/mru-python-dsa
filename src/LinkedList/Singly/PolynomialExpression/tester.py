# Example Usage
from linked_list import LinkedList
poly1 = LinkedList()
poly2 = LinkedList()

print("Polynomial 1:")
poly1.insert_at_end(5, 4)
poly1.insert_at_end(2, 3)
poly1.insert_at_end(6, 1)
poly1.insert_at_end(15, 0)
poly1.traversal()

print("Polynomial 2:")
poly2.insert_at_end(3, 3)
poly2.insert_at_end(8, 1)
poly2.insert_at_end(5, 0)
poly2.traversal()

print("Addition Result:")
result = poly1.add(poly2)
result.traversal()
