from LinkedList import LinkedList

# Testing the LinkedList
if __name__ == "__main__":
    ll = LinkedList()

    print("INSERT AT END:")
    ll.insert_at_end("Chennai")
    ll.insert_at_end("Bangalore")
    ll.insert_at_end("Hyderabad")
    ll.insert_at_end("Mumbai")
    print(f"\nIs 'Chennai' found: {ll.search('Chennai')}")
    ll.traversal()

    ll.insert_at_end("Delhi")
    ll.traversal()

    print("\nINSERT AT BEGINNING:")
    ll.insert_at_beginning("Kochin")
    ll.traversal()

    print("\nINSERT AT POSITION 4:")
    ll.insert_at("Goa", 4)
    ll.traversal()

    print("\nINSERT AT POSITION 12:")
    ll.insert_at("Kashmir", 12)
    ll.traversal()

    print("\nINSERT AT POSITION 1:")
    ll.insert_at("Allapey", 1)
    ll.traversal()

    print("\nDELETE AT END:")
    ll.delete_at_end()
    ll.traversal()

    print("\nDELETE AT BEGINNING:")
    ll.delete_at_beginning()
    ll.traversal()

    print("\nDELETE AT:")
    ll.delete_at("Lucknow")
    ll.traversal()

    ll.delete_at("Hyderabad")
    ll.traversal()

    ll.delete_at("Chennai")
    ll.traversal()

    print("\nDELETE AT END:")
    ll.delete_at_end()
    ll.delete_at_end()
    ll.delete_at_end()
    ll.delete_at_end()
    ll.traversal()

    print(f"\nIs 'Chennai' found: {ll.search('Chennai')}")
