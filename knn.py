from classifier import Classifier
from cls import Class
from dialog import Dialog


class KNearestNeighbors(Classifier):

	def train(self, dialogs: list[Dialog]) -> None:
		return super().train(dialogs)

	def classify(sentence: str) -> Class:
		return super().classify()