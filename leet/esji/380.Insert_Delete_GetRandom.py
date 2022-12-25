#! python

class RandomizedSet:

    def __init__(self):
        self.datas = dict()
        pass

    def insert(self, val: int) -> bool:
        try:
            ret = self.datas[val]
            print(ret)
            return False
        except Exception as e:
            self.datas[val] = True
            return True

    def remove(self, val: int) -> bool:
        try:
            del self.datas[val]
            return True
        except Exception as e:
            return False

    def getRandom(self) -> int:
        pass


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

