class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f'key = {self.key}: value = {self.value} -> {self.next}'


class Hash_table:
    def __init__(self):
        self.data = dict()

    def hash_function(self, key):
        return str(key)[0].upper()

    def cycl_list(self, hash_key, key):
        current = self.data[hash_key]
        previous = None
        while current is not None and current.key != key:
            previous = current
            current = current.next
        return current, previous

    def add_update(self, key, value):
        hash_key = self.hash_function(key)
        if hash_key in self.data.keys():
            current, previous = self.cycl_list(hash_key, key)
            if current is not None:
                current.values = value
                return
            else:
                previous.next = Node(key, value)
        else:
            self.data[hash_key] = Node(key, value)

    def get(self, key):
        hash_key = self.hash_function(key)
        if hash_key not in self.data:
            return f'This key={key} is not valid'
        else:
            current, previous = self.cycl_list(hash_key, key)
            return current.value

    def delete(self, key):
        hash_key = self.hash_function(key)
        if key not in self.data.keys():
            return 'Not in table'
        else:
            current, previous = self.cycl_list(hash_key, key)
            if current is not None:
                if current.next:
                    previous.next = current.next
                else:
                    previous.next = None

    def __str__(self):
        for key, value in self.data.items():
            print(f"{key}:{value}")
        return ''


if __name__ == "__main__":
    ht = Hash_table()
    ht.add_update('Apple', 1.55)
    ht.add_update('Blueberry', 7.30)
    ht.add_update('Strawberry', 3)
    ht.add_update('Milk', 1)
    ht.add_update('Ananas', 5)
    ht.add_update('Juice', 2)
    print(ht)
    ht.add_update('Sok', 2)
    print(ht)
    ht.delete('Milk')
    print(ht)
