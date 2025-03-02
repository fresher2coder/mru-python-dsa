class HashTableChainingKeysOnly:
    """ Hash Table using Separate Chaining - Stores Only Keys (With Delete Function) """

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize empty lists at each index

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        if not isinstance(key, (int, float)):  # Ensure key is a number
            raise ValueError("Only numeric keys are allowed!")

        index = self.hash_function(key)

        if key not in self.table[index]:  # Avoid duplicates
            self.table[index].append(key)

    def search(self, key):
        index = self.hash_function(key)
        return key in self.table[index]  # Returns True if key exists, else False

    def delete(self, key):
        index = self.hash_function(key)

        if key in self.table[index]:  # Check if the key exists
            self.table[index].remove(key)
            print(f"Key {key} deleted successfully.")
        else:
            print(f"Key {key} not found.")

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


# Example usage
ht_chain_keys = HashTableChainingKeysOnly(10)
ht_chain_keys.insert(15)
ht_chain_keys.insert(25)  # Collision handled
ht_chain_keys.insert(35)
ht_chain_keys.display()

# Deleting keys
ht_chain_keys.delete(25)  # ✅ Key exists, so it's deleted
ht_chain_keys.delete(50)  # ❌ Key doesn't exist
ht_chain_keys.display()
