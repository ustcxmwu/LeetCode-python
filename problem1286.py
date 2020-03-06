import itertools


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.data = ["".join(combination) for combination in itertools.combinations(characters, combinationLength)]
        self.cur = -1

    def next(self) -> str:
        self.cur += 1
        return self.data[self.cur]

    def hasNext(self) -> bool:
        return True if self.cur+1 < len(self.data) else False


if __name__ == '__main__':

    result = itertools.combinations("abcd",2)
    print(type(result))
    print(list(result))