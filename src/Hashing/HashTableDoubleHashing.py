class HashTableDoubleHashing:
    """ Hash Table using Double Hashing with Active, Deactivated, and None states """

    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function1(self, key):
        return key % self.size

    def hash_function2(self, key):
        return 1 + (key % (self.size - 1))  # Ensures step size is nonzero

    def insert(self, key):
        if not isinstance(key, (int, float)):
            raise ValueError("Only numeric keys are allowed!")

        index = self.hash_function1(key)
        step = self.hash_function2(key)
        i = 0

        # Double Hashing: Find next available slot (None or "DELETED")
        while self.table[(index + i * step) % self.size] not in [None, "DELETED"]:
            if self.table[(index + i * step) % self.size] == key:
                return  # Avoid duplicate insertion
            i += 1
            if i == self.size:
                raise Exception("Hash table is full")

        self.table[(index + i * step) % self.size] = key  # Insert key

    def search(self, key):
        index = self.hash_function1(key)
        step = self.hash_function2(key)
        i = 0

        while self.table[(index + i * step) % self.size] is not None:  # Stops only at None
            if self.table[(index + i * step) % self.size] == key:
                return True
            i += 1
            if i == self.size:
                break
        return False

    def delete(self, key):
        index = self.hash_function1(key)
        step = self.hash_function2(key)
        i = 0

        while self.table[(index + i * step) % self.size] is not None:  # Stops only at None
            if self.table[(index + i * step) % self.size] == key:
                self.table[(index + i * step) % self.size] = "DELETED"
                print(f"Key {key} deleted successfully.")
                return
            i += 1
            if i == self.size:
                break

        print(f"Key {key} not found.")

    def display(self):
        print(self.table)

# Example usage
ht_double = HashTableDoubleHashing(10)
ht_double.insert(15)
ht_double.insert(25)  # Collision handled by double hashing
ht_double.insert(35)
ht_double.display()

ht_double.delete(25)  # ✅ Marked as "DELETED"
ht_double.display()

print(ht_double.search(25))  # ❌ False (search skips "DELETED", keeps looking)
ht_double.insert(45)  # ✅ Reuses "DELETED" slot
ht_double.display()
