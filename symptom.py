
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Symptom(ABC):

	__sentences: dict[str, list[str]]
	__features: dict[str, list[int|float]] = field(init=False)
	_bag: dict[str, int] = field(init=False, default_factory=dict)

	def __post_init__(self) -> None:
		"""creates a bag of words (word: index dictionary )"""
		current_index = 0

		for _, sentences in self.__sentences.items():
			for sentence in sentences:
				for word in sentence.split():
					if word not in self._bag:
						self._bag[word] = current_index
						current_index += 1
	
		self.make_features()
	
	@abstractmethod
	def make_features(self):
		"""vectorizes training data"""
		self.__features = { cls: [self.vectorize(sentence) for sentence in sentences ] for cls, sentences in self.__sentences.items() }

	@abstractmethod
	def vectorize(self, sentence: str) -> list[float|int]:
		"""converts a sentence into a vector"""
		pass

	def bag(self) -> dict[str, int]:
		"""returns the bag of words"""
		return self._bag

	def features(self) -> dict[str, list[int|float]]:
		"""returns feature vectors for individual classes"""
		return self.__features
	
	def _sentences(self) -> dict[str, list[str]]:
		"""returns all sentences"""
		return self.__sentences
