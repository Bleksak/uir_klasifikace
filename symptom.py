from functools import reduce
import math
from operator import attrgetter
from bag import BagOfWords
from cls import Class
from dialog import Dialog


def make_corpus(cls: Class, dialogs: list[Dialog]) -> list[str]:
    """splits dialogs into separate classes (corpus)"""
    return list(map(attrgetter('text'), filter(lambda document: document.cls == cls, dialogs)))

def bow_sublist(dialogs: list[str]) -> list[BagOfWords]:
    return [BagOfWords(sentence.split()) for sentence in dialogs]

def bow(classes: set[Class], dialogs: list[Dialog]) -> dict[Class, dict[str, float]]:
	return {cls: {k:1/v for k,v in reduce_bow(bow_sublist(make_corpus(cls, dialogs))).items()} for cls in classes}

def count_distinct(documents: list[str]) -> int:
    return len(set("".join(documents).split()))

def reduce_bow(corpus: list[BagOfWords]) -> dict[str, int]:
    return reduce(lambda a, b: a.update(b), corpus, BagOfWords())

def document_frequency_calculate(bag: dict[str, int]) -> BagOfWords:
    """calculates the actual document frequency"""
    return {word: (bag[word]+1) / (sum(bag.values()) + sum(1 if x > 0 else 0 for x in bag.values()) + 1) for word in bag}

def document_frequency(classes: set[Class], dialogs: list[Dialog]) -> dict[Class, dict[str, float]]:
    return {cls : document_frequency_calculate(reduce_bow(bow_sublist(make_corpus(cls, dialogs)))) for cls in classes}

def tf(term: str, bag: dict[str, int]) -> float:
    """"calculates the term frequency for given term and document"""
    return bag.get(term, 0) / len(bag)

def idf(term: str, bag: list[dict[str, int]]) -> float:
    """calculates the inverse document frequency for given term and corpus"""
    return math.log10(len(bag) / sum( 1 if dialog.get(term, 0) > 0 else 0 for dialog in bag))

def tfidf_calculate(term: str, bag: dict[str, int], corpus: list[dict[str, int]]) -> float:
    """calculates the actual tf-idf value"""
    return tf(term, bag) * idf(term, corpus)

def tfidf_each(bags: list[BagOfWords]) -> dict[str, float]:
    d = {}

    for bag in bags:
        for term in bag:
            d[term] = d.get(term, 0) + tfidf_calculate(term, bag, bags)

    for item, value in d.items():
        d[item] = value / len(d)

    return d

def tfidf(classes: set[Class], dialogs: list[Dialog]) -> dict[Class, dict[str,  float]]:
    return {cls: tfidf_each(bow_sublist(make_corpus(cls, dialogs))) for cls in classes}

