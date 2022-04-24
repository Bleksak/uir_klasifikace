from dataclasses import dataclass
from typing import Counter

from symptom import Symptom

@dataclass
class DocumentFrequency(Symptom):
	def vectorize(self, sentence: str):
		"""converts a sentence into a vector"""
		v = [0] * len(self._bag)

		for word, count in Counter(sentence.split()).items():
			if word in self._bag:
				v[ self._bag[word] ] = count
		
		return v
	