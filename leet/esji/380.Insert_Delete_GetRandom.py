#! python
import random


class RandomizedSet:

    def __init__(self):
        self.tbl_key = list()
        self.datas = dict()
        pass

    def insert(self, val: int) -> bool:


    def remove(self, val: int) -> bool:


    def getRandom(self) -> int:


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

