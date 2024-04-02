# Hash table with chaining implementation in Python
class ChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Create empty table with empty lists for chaining

    # Hash function to determine the index of the key
    def hash_function(self, key):
        return hash(key) % self.size  # Simple hash function

    # Method to insert a key-value pair into the hash table
    def cht_insert(self, key, value):
        index = self.hash_function(key)
        # Check for existing key and update
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # If key not found, insert new key-value pair
        self.table[index].append((key, value))

    # Method to retrieve the value associated with a key
    def get_value(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Key not found

    # Method to remove a key-value pair from the hash table
    def remove(self, key):
        index = self.hash_function(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True  # Key removed successfully
        return False  # Key not found

    def print_table_values(self):
        packages = []
        for bucket in self.table:
            for k, v in bucket:
                packages.append(v)
        # Sort by an attribute of the objects, e.g., 'id'
        packages.sort(key=lambda x: x.package_id)  # Replace 'id' with the actual attribute you want to sort by
        for p in packages:
            print(f"{p}")

    # Method to search for a key in the hash table
    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Key not found

    def get_all(self):
        all_values = []
        for bucket in self.table:
            for k, v in bucket:
                print(f"Key: {k}, Value: {v}")
                all_values.append((k, v))
        return all_values

    def print_all_values(self):
        all_values = []
        for bucket in self.table:
            for k, v in bucket:
                print(f"{v}")
                all_values.append((k, v))
        return all_values
