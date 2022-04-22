from typing import Counter


class BagOfWords(Counter):
	def update(self, x):
		super().update(x)
		return self
	
	# def vectorize(self, sentence: str):
	# 	"""vectorizes a string"""
	# 	return [ value for word in sentence.split() for key, value in self.items() if word == key]
