from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from cls import Row
from symptom import Symptom

@dataclass(frozen=True)
class Classifier(ABC):
    """defines the classifier abstract class"""

    classes: field(dict[str, Row], default_factory=dict, init=True)
    symptom: Symptom

    @abstractmethod
    def classify(sentence) -> Row:
        pass
