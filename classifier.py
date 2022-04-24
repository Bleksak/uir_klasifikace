from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Callable
from symptom import Symptom


@dataclass
class Classifier(ABC):
    """defines the classifier abstract class"""

    classes: list[str]
    symptom_class: Callable[[dict[str, list[str]]], None]
    symptom: Symptom = field(init=False)

    @abstractmethod
    def train(self, dialogs: dict[str, list[str]]) -> None:
        """trains the classifier, this must be called before calling classify"""
        self.symptom = self.symptom_class(dialogs)

    @abstractmethod
    def classify(sentence: str) -> str:
        """classifies the sentence into one of classes, classifier must be trained before calling this method, otherwise random result will be returned"""
        pass
