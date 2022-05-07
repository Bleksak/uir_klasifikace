from dataclasses import dataclass
from functools import partial
from operator import itemgetter
from typing import Callable, Counter
from classifier import Classifier
from distance import euclidean, manhattan, cosine

@dataclass
class KNearestNeighbors(Classifier):
	"""The K Nearest Neighbors classifier"""

	distance_fn: Callable[ [list[float], list[float]], float ] = cosine
	"""distance function used (euclidean, cosine, manhattan)"""
	k: int = 3
	"""default value of k"""

	def train(self, dialogs: dict[str, list[str]]) -> None:
		super().train(dialogs)
	
	def classify(self, sentence: str) -> str:
		"""classifies a sentence into a class"""

		distance = partial(self.distance_fn, self.symptom.vectorize(sentence))

		k_values = []
		k_keys = []

		for cls, features in self.symptom.features().items():
			for feature in features:
				k_values.append(distance(feature))
				k_keys.append(cls)
		

		return Counter(sorted(zip(k_keys, k_values), key=itemgetter(1))[:self.k]).most_common(1)[0][0][0]
