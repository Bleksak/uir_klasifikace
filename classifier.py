from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable
from cls import Class
from dialog import Dialog


@dataclass
class Classifier(ABC):
    """defines the classifier abstract class"""

    classes: set[Class]
    symptom: Callable[[ set[Class], list[Dialog] ], dict[Class, dict[str, float]]]

    @abstractmethod
    def train(self, dialogs: list[Dialog]) -> None:
        """trains the classifier, this must be called before calling classify"""
        pass

    @abstractmethod
    def classify(sentence: str) -> Class:
        """classifies the sentence into one of classes, classifier must be trained before calling this method, otherwise random result will be returned"""
        pass
