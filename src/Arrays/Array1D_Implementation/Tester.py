from Array import Array1D

# Tester class
def test_Array1D():
    print("--- Testing Array1D ---")

    arr = Array1D(5)

    # Test isEmpty on empty array
    print("Initial array:", arr.getArray())
    print("Is array empty?", arr.isEmpty())

    # Test append
    arr.append(10)
    arr.append(20)
    arr.append(30)
    print("After appending 10, 20, 30:", arr.getArray())

    # Test insert
    arr.insert(15, 1)  # Insert 15 at index 1
    print("After inserting 15 at index 1:", arr.getArray())

    # Test deleteAt
    arr.deleteAt(2)  # Delete element at index 2
    print("After deleting element at index 2:", arr.getArray())

    # Test deleteValue
    arr.deleteValue(15)  # Delete value 15
    print("After deleting value 15:", arr.getArray())

    # Test deleteBegin
    arr.deleteBegin()
    print("After deleting at the beginning:", arr.getArray())

    # Test deleteEnd
    arr.deleteEnd()
    print("After deleting at the end:", arr.getArray())

    # Test traversal
    arr.traversal()

    # Test isFull
    arr.append(40)
    arr.append(50)
    arr.append(60)
    print("After appending 40, 50, 60:", arr.getArray())
    print("Is array full?", arr.isFull())

    # Test appending to a full array
    arr.append(70)

    # Final state
    arr.traversal()

if __name__ == "__main__":
    test_Array1D()
