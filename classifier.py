from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from symptom import DocumentFrequency, Symptom
from cls import Class
from dialog import Dialog


@dataclass
class Classifier(ABC):
    """defines the classifier abstract class"""

    classes: set[Class]
    symptom: Symptom = DocumentFrequency()
    class_counts: dict[Class, int] = field(init=False, default_factory=dict)
    train_data: list[Dialog] = field(init=False)
    count: int = 0

    def train(self, dialogs: list[Dialog]):
        self.class_counts = {cls:0 for cls in self.classes}

        for dialog in dialogs:
            self.class_counts[dialog.cls] += 1
            self.count += 1
            # TODO: symptoms
        
        

    @abstractmethod
    def classify(sentence) -> Class:
        pass
