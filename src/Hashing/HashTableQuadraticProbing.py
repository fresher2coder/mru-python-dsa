class HashTableQuadraticProbing:
    """ Hash Table using Quadratic Probing with Active, Deactivated, and None states """

    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        if not isinstance(key, (int, float)):
            raise ValueError("Only numeric keys are allowed!")

        index = self.hash_function(key)
        i = 0

        # Quadratic Probing: Find next available slot (None or "DELETED")
        while self.table[(index + i ** 2) % self.size] not in [None, "DELETED"]:
            if self.table[(index + i ** 2) % self.size] == key:
                return  # Avoid duplicate insertion
            i += 1
            if i == self.size:
                raise Exception("Hash table is full")

        self.table[(index + i ** 2) % self.size] = key  # Insert key

    def search(self, key):
        index = self.hash_function(key)
        i = 0

        while self.table[(index + i ** 2) % self.size] is not None:  # Stops only at None
            if self.table[(index + i ** 2) % self.size] == key:
                return True
            i += 1
            if i == self.size:
                break
        return False

    def delete(self, key):
        index = self.hash_function(key)
        i = 0

        while self.table[(index + i ** 2) % self.size] is not None:  # Stops only at None
            if self.table[(index + i ** 2) % self.size] == key:
                self.table[(index + i ** 2) % self.size] = "DELETED"
                print(f"Key {key} deleted successfully.")
                return
            i += 1
            if i == self.size:
                break

        print(f"Key {key} not found.")

    def display(self):
        print(self.table)

# Example usage
ht_quadratic = HashTableQuadraticProbing(10)
ht_quadratic.insert(15)
ht_quadratic.insert(25)  # Collision handled by quadratic probing
ht_quadratic.insert(35)
ht_quadratic.display()

ht_quadratic.delete(25)  # ✅ Marked as "DELETED"
ht_quadratic.display()

print(ht_quadratic.search(25))  # ❌ False (search skips "DELETED", keeps looking)
ht_quadratic.insert(45)  # ✅ Reuses "DELETED" slot
ht_quadratic.display()
