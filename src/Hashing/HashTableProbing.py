class HashTableProbing:
    """ Hash Table with Linear Probing and State Management (Active, Deactivated, None) """

    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Initialize table with None

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        if not isinstance(key, (int, float)):
            raise ValueError("Only numeric keys are allowed!")

        index = self.hash_function(key)

        # Linear Probing: Find next available slot (None or "DELETED")
        while self.table[index] not in [None, "DELETED"]:
            if self.table[index] == key:  # Avoid duplicate insertion
                return
            index = (index + 1) % self.size

        self.table[index] = key  # Insert key

    def search(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:  # Stops only at None, not "DELETED"
            if self.table[index] == key:
                return True  # Key found
            index = (index + 1) % self.size
            if index == start_index:
                break
        return False  # Key not found

    def delete(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:  # Stops only at None, not "DELETED"
            if self.table[index] == key:
                self.table[index] = "DELETED"  # Mark as deactivated
                print(f"Key {key} deleted successfully.")
                return
            index = (index + 1) % self.size
            if index == start_index:
                break

        print(f"Key {key} not found.")

    def display(self):
        print(self.table)

# Example usage
ht = HashTableProbing(10)
ht.insert(15)
ht.insert(25)  # Collision handled by linear probing
ht.insert(35)
ht.display()

ht.delete(25)  # ✅ Key is marked as "DELETED"
ht.display()

print(ht.search(25))  # ❌ False (Search skips "DELETED", keeps looking)
ht.insert(45)  # ✅ Reuses "DELETED" slot
ht.display()
