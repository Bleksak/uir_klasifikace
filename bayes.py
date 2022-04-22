from dataclasses import dataclass, field
from operator import itemgetter
from classifier import Classifier
from cls import Class
from dialog import Dialog


@dataclass
class Bayes(Classifier):
	"""naive bayes classifier implementation"""

	class_probabilities: dict[Class, float] = field(default_factory=dict, init=False)
	probabilities: dict[Class, dict[str, float]] = field(init=False)

	def train(self, dialogs: list[Dialog]):

		# 1. calculate P(class)
		# 2. calculate P(word | class):
		# -- word frequency for each class
		# -- distinct word count for each class

		N = len(dialogs)

		for cls in self.classes:
			count = sum(1 for _ in filter(lambda x: x.cls == cls, dialogs))
			self.class_probabilities[cls] = count / N
		
		self.probabilities = self.symptom(self.classes, dialogs)

		print(self.class_probabilities)
		print(self.probabilities)

	def classify(self, sentence: str) -> Class:
		probabilities = {}

		for cls in self.classes:
			p = 1
			for word in sentence.split():
				p *= self.probabilities[cls].get(word.strip('.,-!'), 1)
			
			probabilities[cls] = p

		return min(probabilities.items(), key=itemgetter(1))[0]