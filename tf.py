from dataclasses import dataclass
from typing import Counter

from symptom import Symptom

@dataclass
class TermFrequency(Symptom):
	"""Term Frequency smymptom"""

	def make_features(self):
		return super().make_features()

	def vectorize(self, sentence: str) -> list[float|int]:
		"""converts a sentence into a vector x where for each word x[word] = word count / number of words"""
		v = [0] * len(self._bag)

		split = sentence.split()
		counter = Counter(split)

		for word, count in counter.items():
			if word in self._bag:
				v[self._bag[ word ]] = count / len(split)

		return v