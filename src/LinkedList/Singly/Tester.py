from linked_list import LinkedList

trip = LinkedList()

trip.insertAtEnd("Chennai", "TN", 600059)
trip.insertAtEnd("Bangalore", "KT", 700059)
trip.insertAtEnd("Hyderabad", "TL", 800059)
trip.insertAtEnd("Mumbai", "MH", 900059)
trip.traversal()

trip.insertAtBeginning("Kochin", "KR", 501254)
trip.traversal()

trip.insertAt(0, city="Goa", state="Goa", pincode=125784)
trip.traversal()

trip.insertAt(6, city="Delhi", state="Delhi", pincode=215784)
trip.traversal()

trip.insertAt(5, city="Secundrabad", state="TL", pincode=412563)
trip.traversal()

