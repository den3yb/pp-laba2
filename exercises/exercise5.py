import os

from exercise4 import get
from typing import Optional


class otzovik:
    def __init__(self, dataset: str, rait: str):
        self.counter = 0
        self.dataset = dataset
        self.rait = rait
        self.limit = 0
        self.limit += len(os.listdir(os.path.join(dataset, rait)))
        print("LIMIT:", self.limit)

    def __iter__(self) -> None:
        return self

    def __next__(self) -> str:

        if self.counter < self.limit:
            temp = get(self.dataset, self.rait, self.counter)
            self.counter += 1
            return temp
        else:
            raise StopIteration


test = otzovik("C:\Proganiy\Git PP\dataset", "4")

for val in test:
    print(val)
