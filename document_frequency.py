from dataclasses import dataclass
from typing import Counter

from symptom import Symptom

@dataclass
class DocumentFrequency(Symptom):
	"""Document Frequency symptom"""

	def make_features(self):
		return super().make_features()

	def vectorize(self, sentence: str) -> list[float|int]:
		"""converts a sentence into a vector, where each vector field = count of each individual words"""
		v = [0] * len(self._bag)

		for word, count in Counter(sentence.split()).items():
			if word in self._bag:
				v[ self._bag[word] ] = count
		
		return v
	