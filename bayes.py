from dataclasses import dataclass, field
from functools import reduce
from operator import itemgetter
from classifier import Classifier

@dataclass
class Bayes(Classifier):
	"""naive bayes classifier implementation"""

	class_probabilities: dict[str, float] = field(init=False)
	probabilities: dict[str, dict[str, float]] = field(init=False, default_factory=dict)
	laplace_smoothing: int = 1

	def train(self, dialogs: dict[str, list[str]]) -> None:
		super().train(dialogs)

		count = sum(len(sentences) for _, sentences in dialogs.items())
		self.class_probabilities = {cls: len(sentences) / count for cls, sentences in dialogs.items()}

		vec = self.symptom.vectorize('')

		distinct_words_count = self.laplace_smoothing * len(vec)

		for cls, features in self.symptom.features().items():
			one_word_sum = [self.laplace_smoothing + sum(x) for x in (zip(*features))]
			all_words_sum = sum(sum(x) for x in zip(*features))

			self.probabilities[cls] = [x / (distinct_words_count + all_words_sum) for x in one_word_sum]

	def classify(self, sentence: str) -> str | None:
		symptom = self.symptom.vectorize(sentence)

		max_p = 0 
		max_cls = None

		for cls in self.classes:
			p = self.class_probabilities.get(cls, 0)

			for index, value in enumerate(symptom):
				p *= self.probabilities[cls][index] ** value
			
			if p > max_p:
				max_p = p
				max_cls = cls
		
		return max_cls