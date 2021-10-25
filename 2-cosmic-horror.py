import pickle

class Strack:
    def __init__(self):
        self.data = b""
        self.indexes = "0"
        self.index_indexes = "0"

    def pop(self):
        val = self.data[-int(self.indexes[-(int(self.index_indexes[-1])):]):]
        self.data = self.data[:-int(self.indexes[-(int(self.index_indexes[-1])):])]
        self.indexes = self.indexes[:-int(self.index_indexes[-1])]
        self.index_indexes = self.index_indexes[:-1]
        return pickle.loads(val)

    def push(self, data):
        data = pickle.dumps(data)
        self.data += data
        self.indexes += str(len(data))
        self.index_indexes += str(len(str(len(data))))


if __name__ == "__main__":
    strack = Strack()
    strack.push(7)
    strack.push("hello")
    strack.push([1, 2, 3])
    print(strack.pop())
    print(strack.pop())
    print(strack.pop())

