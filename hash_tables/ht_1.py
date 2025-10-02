class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
        
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])


    def __hash(self, key):
        my_hash = 0
        'dfdf'
        for letter in key:
            my_hash = (my_hash +ord(letter)*23) % len(self.data_map)
            
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)





my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1400)
my_hash_table.print_table()
