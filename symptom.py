
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Symptom(ABC):

	__sentences: dict[str, list[str]]
	_features: dict[str, list[int|float]] = field(init=False)
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
		
		self._features = { cls: [self.vectorize(sentence) for sentence in sentences ] for cls, sentences in self.__sentences.items() }

	@abstractmethod
	def vectorize(self, sentence: str) -> list[float|int]:
		pass

	def bag(self) -> dict[str, int]:
		return self._bag

	def features(self) -> dict[str, list[int|float]]:
		return self._features