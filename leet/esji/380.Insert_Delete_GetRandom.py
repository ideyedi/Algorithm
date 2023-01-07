#! python
import random


class RandomizedSet:

    def __init__(self):
        self.tbl_key = dict()
        self.data = list()
        pass

    def insert(self, val: int) -> bool:
        if val in self.tbl_key:
            return False

        self.data.append(val)
        self.tbl_key[val] = self.data.index(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.tbl_key:
            return False

        i = self.tbl_key[val]
        self.tbl_key[self.data[-1]] = i
        self.data[i] = self.data[-1]

        self.tbl_key.pop(val)
        self.data.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


if __name__ == "__main__":
    # Your RandomizedSet object will be instantiated and called as such:
    obj = RandomizedSet()
    param_1 = obj.insert(1)
    print(param_1)
    param_2 = obj.remove(2)
    print(param_2)
    param_3 = obj.insert(2)
    print(param_3)
    param_3 = obj.getRandom()
    print(param_3)
    param_2 = obj.remove(1)
    print(param_2)
    param_1 = obj.insert(2)
    print(param_1)
    param_3 = obj.getRandom()
    print(param_3)