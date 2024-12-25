from typing import Any


class FancyTuple:
    def __init__(self, *params):
        self.params = params

    def __len__(self):
        return len(self.params)

    def __getattr__(self, name):
        base = ["first", "second", "third", "fourth", "fifth"]
        if name in base:
            index = base.index(name)
            if index < len(self.params):
                return self.params[index]
            raise AttributeError(f"Index {index} is out of range")
        raise AttributeError(f"'FancyTuple' object has no attribute '{name}'")

    def __str__(self):
        return str(self.params)

    def __repr__(self):
        return f"FancyTuple{self.params}"


params = ["dog", "cat", "cow"]
ds = FancyTuple(*params)
print(ds.first)  # prints: dog
print(ds.second)  # prints: cat
print(len(ds))  # prints: 3
