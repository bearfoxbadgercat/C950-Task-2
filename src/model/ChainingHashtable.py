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

    # Method to print the hash table
    def print_table(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

    def print_table_values(self):
        packages = []
        for bucket in self.table:
               for k,v in bucket:
                   packages.append(v)
        for p in packages:
            print(f"{p}")

    # Method to search for a key in the hash table
    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Key not found

    # Method to return key based on value
    def get_key(self, value):
        for bucket in self.table:
            for k, v in bucket:
                if v == value:
                    return k
        return None  # Value not found

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

    def get_nested_value(self, outer_key, inner_key):
        outer_index = self.hash_function(outer_key)
        for k, inner_table in self.table[outer_index]:
            if k == outer_key:
                for inner_k, v in inner_table:
                    if inner_k == inner_key:
                        return v
        return None  # Either outer or inner key not found

    # Method to print value as a string

