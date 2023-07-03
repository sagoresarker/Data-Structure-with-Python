class HashTable:
    def __init__(self, size=7):
        self.data_map = [None]*size

    def _hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23)%len(self.data_map)

        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self._hash(key)

        if self.data_map[index] == None:
            self.data_map[index] = []
        
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self._hash(key)

        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        
        return all_keys

my_hash = HashTable()
my_hash.set_item('A', 12)
my_hash.set_item('B', 13)
my_hash.set_item('C', 14)
my_hash.set_item('D', 15)
my_hash.set_item('E', 16)

print('\nGet Method: ', my_hash.get_item('A'))
my_hash.print_table()

print(my_hash.keys())