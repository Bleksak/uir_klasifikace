from abc import ABC, abstractmethod
from operator import itemgetter


class Symptom(ABC):
    @abstractmethod
    def make(self, sentence: str) -> list[int]:
        return []


class DocumentFrequency(Symptom):
    def __count_words(self, text: str) -> tuple[str, int]:
        d: dict[str:int] = {}
        for word in map(lambda item: item.lower().strip('`.\'":'), text.split()):
            if word:
                d[word] = d.get(word, 0) + 1

        return d.items()

    def make(self, sentence: str) -> list[int]:
        words = self.__count_words(sentence)
        s = sum(words, itemgetter(1))

        return {word[0]: word[1]/s for word in words}


class TFID(Symptom):
    def make(sentence: str) -> list[int]:
        return []


class MutualInformation(Symptom):
    def make(sentence: str) -> list[int]:
        return []
