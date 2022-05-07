from dataclasses import dataclass, field
from typing import Counter

from tf import TermFrequency

@dataclass
class TFIDF(TermFrequency):

	__idf: list[float] = field(init=False)

	def make_features(self):
		self.__make_idf()
		super().make_features()

	def __make_idf(self):
		import math
		sentences_count = 0

		self.__idf = [0] * len(self._bag)

		for _, sentences in self._sentences().items():
			sentences_count += len(sentences)
			
			for sentence in sentences:
				unique_words = set()

				for word in sentence.split():
					if word not in unique_words:
						unique_words.add(word)
						self.__idf[ self._bag[word] ] += 1

		for i,v in enumerate(self.__idf):
			self.__idf[i] = math.log10(sentences_count / v)
		
	def vectorize(self, sentence: str) -> list[float|int]:
		"""converts a sentence into a vector"""
		return [tf * idf for tf, idf in zip(super().vectorize(sentence), self.__idf)]
	