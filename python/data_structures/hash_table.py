class HashTable:
    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(size)]
        self.num_elements = 0

    def _calculate_load_factor(self):
        return self.num_elements / self.size

    def get_index(self, key):
        return hash(key) % self.size

    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.num_elements = 0

        for bucket in old_table:
            for key, value in bucket:
                self.add_or_update(key, value)

    def add_or_update(self, key, value):
        index = self.get_index(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.num_elements += 1

        if self._calculate_load_factor() > 0.7:
            self._resize()

    def get(self, key):
        index = self.get_index(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        index = self.get_index(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                self.num_elements -= 1
                return
        raise KeyError(f"Key '{key}' not found")

    def __str__(self) -> str:
        items = []
        for bucket in self.table:
            if bucket:
                items.extend(bucket)
        return str(dict(items))
