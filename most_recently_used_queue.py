# 1756

class MRUQueue:

    def __init__(self, n: int):
        self.data = [i for i in range(n)] # zero index add 1 to all values

    def fetch(self, k: int) -> int:
        val = self.data.pop(k - 1)
        self.data.append(val)
        return val + 1


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)