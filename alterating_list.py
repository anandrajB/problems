class AlternatingList:

    def __init__(self, seq):
        self.seq = seq
        self.length = len(seq)

    def __iter__(self):
        for i in range(self.length // 2):
            yield self.seq[i]
            print("the plsu", -(i + 1))
            print("the sqt", self.seq[-(i + 1)])
            yield self.seq[-(i + 1)]
        if self.length % 2 != 0:
            yield self.seq[self.length // 2]


seq = "1 2 3 4"
w = AlternatingList(seq)


for e in w:
    print(str(e))
