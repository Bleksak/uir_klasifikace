from dataclasses import dataclass, field
from classifier import Classifier
from cls import Class
from dialog import Dialog


@dataclass
class Bayes(Classifier):
    """naive bayes classifier implementation"""

    probabilities: dict[Class, float] = field(default_factory=dict, init=False)
    # prob_count: field(int, init=False)

    def train(self, dialogs: list[Dialog]):
        super().train(dialogs)

        for cls in self.classes:
            self.probabilities[cls] = self.class_counts[cls] / self.count

    def classify(sentence: str) -> Class:
        # n = YES count
        # nc = SUV + YES count
        # p = 1 / pocet trid
        # m = vyber si sam curaku



        pass