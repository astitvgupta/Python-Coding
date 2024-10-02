class Encoding:
    n = int(input())
    # tuple = ()
    def hashing(self):
        for i in range(0, self.n):
            val = input().split(" ")
            tupl = tuple(map(int, val))
            return tupl
            # print(tupl, hash(tupl))

obj = Encoding()
print(hash(obj.hashing()))