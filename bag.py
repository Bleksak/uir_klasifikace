from typing import Counter


class BagOfWords(Counter):
    def update(self, x):
        super().update(x)
        return self