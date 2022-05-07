import math
import operator

def euclidean(vec1: list[float], vec2: list[float]) -> float:
	"""returns the euclidean distance of two vectors"""
	return sum(map(lambda a,b: (a-b)**2, vec1, vec2))

def manhattan(vec1: list[float], vec2: list[float]) -> float:
	"""returns the manhattan distance of two vectors"""
	return sum(map(operator.sub, vec1, vec2))

def dot(vec1: list[float], vec2: list[float]) -> float:
	"""returns the dot product of two vectors"""
	return sum(map(operator.mul, vec1, vec2))

def norm(vec: list[float]) -> float:
	"""returns the euclidian norm of a vector"""
	return math.sqrt(sum(x*x for x in vec))

def cosine(vec1: list[float], vec2: list[float]) -> float:
	"""returns the cosine distance of two vectors"""
	n1 = norm(vec1)
	n2 = norm(vec2)
	if n1 == 0 or n2 == 0:
		return 0

	return dot(vec1, vec2) / (n1 * n2)
