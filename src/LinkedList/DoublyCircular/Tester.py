from linked_list import DoublyCircularLinkedList

# Initialize the LinkedList
trip = DoublyCircularLinkedList()

# Insert at the end
print("Insert at the end:")
trip.insertAtEnd("Chennai", "TN", 600059)
trip.insertAtEnd("Bangalore", "KT", 700059)
trip.insertAtEnd("Hyderabad", "TL", 800059)
trip.insertAtEnd("Mumbai", "MH", 900059)
trip.traversal()

# Insert at the beginning
print("\nInsert at the beginning:")
trip.insertAtBeginning("Kochin", "KR", 501254)
trip.traversal()

# Insert at a specific index
print("\nInsert at index 0:")
trip.insertAt(0, city="Goa", state="Goa", pincode=125784)
trip.traversal()

print("\nInsert at the last index (index 6):")
trip.insertAt(6, city="Delhi", state="Delhi", pincode=215784)
trip.traversal()

print("\nInsert at index 5:")
trip.insertAt(5, city="Secundrabad", state="TL", pincode=412563)
trip.traversal()

# Delete from the beginning
print("\nDelete at the beginning:")
trip.deleteAtBegin()
trip.traversal()

# Delete from the end
print("\nDelete at the end:")
trip.deleteAtEnd()
trip.traversal()

# Delete at a specific index
print("\nDelete at index 3:")
trip.deleteAt(3)
trip.traversal()

# Remove by value
print("\nRemove by value (Hyderabad):")
trip.removeAt("Hyderabad")
trip.traversal()

print("\nRemove by value (Non-existent city):")
trip.removeAt("Pune")
trip.traversal()

# Search for a value
print("\nSearch for 'Mumbai':")
trip.search("Mumbai")

print("\nSearch for 'Pune':")
trip.search("Pune")

