from dataclasses import dataclass, field
from operator import attrgetter
from classifier import Classifier
from cls import Row


@dataclass
class Bayes(Classifier):
    """naive bayes classifier implementation"""

    probabilities: field(dict[Row, float], default_factory=dict, init=False)
    prob_count: field(int, init=False)

    def __post_init__(self):
        n = sum(self.classes, attrgetter('count'))
        for cls in self.classes:
            self.probabilities[cls] = cls.count / n


    def classify(sentence) -> Row:
        # n = YES count
        # nc = SUV + YES count
        # p = 1 / pocet trid
        # m = vyber si sam curaku

        

        pass