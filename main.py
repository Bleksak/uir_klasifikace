import json
import sys
from classifier import Classifier
from document_frequency import DocumentFrequency
from bayes import Bayes
from knn import KNearestNeighbors
from symptom import Symptom
import pickle

from tf import TermFrequency
from tfidf import TFIDF

symptoms = {
	'df': DocumentFrequency,
	'tf': TermFrequency,
	'tfidf': TFIDF
}

classifiers = {
	'bayes': Bayes,
	'knn': KNearestNeighbors
}

CLASS_LIST_FILE = 'DA_tridy.txt'

def load_zappe(filename: str, classes: list[str]) -> dict[str, list[str]]:
	loaded_dialogs = {cls: [] for cls in classes}

	with open(filename) as file:
		for line in file.readlines():
			line = line.split()
			cls = line[0]
			rest = " ".join(line[1:])
			loaded_dialogs[cls].append(rest)
	
	return loaded_dialogs

def run_with_model(model):
	def get_classifier(model):
		with open(f'{model}.classifier', 'rb') as f:
			return pickle.load(f)
	def get_data(model):
		with open(f'{model}.data', 'rb') as f:
			return pickle.load(f)

	classifier = get_classifier(model)
	data = get_data(model)

	accuracy = sum(1 for item in data if item[0] == item[1]) / len(data)

	print('accuracy - prints accuracy of the classifier')
	print('sentence - input a sentence and try to classify')
	print('quit - quits the program')
	
	while True:

		cmd = input('> ')

		match cmd:
			case 'accuracy':
				print(f'The accuracy of the classifier is: {accuracy}')
				pass
			case 'sentence':
				sentence = input('Enter a sentence: ')
				classified = classifier.classify(sentence)
				print(f'Sentence classified as: {classified}')
			case 'quit':
				break

def train_model(train: dict[str, list[str]], test: dict[str, list[str]], classifier: Classifier, model):
	classifier.train(train)

	# (expected, got, sentence)
	log = [(expected, classifier.classify(sentence), sentence) for expected, sentences in test.items() for sentence in sentences]

	with open(f'{model}.classifier', 'wb') as f:
		pickle.dump(classifier, f)
	
	with open(f'{model}.data', 'wb') as f:
		pickle.dump(log, f)


def main(argv: list[str]) -> int:

	if len(argv) > 2:
		classlist_file = argv[1]
		train_file = argv[2]
		test_file = argv[3]
		symptom_alg_name = argv[4]
		classifier_name = argv[5]
		model_name = argv[6]

		classlist = [line.strip() for line in open(classlist_file).readlines()]
		train = load_zappe(train_file, classlist)
		test = load_zappe(test_file, classlist)
		symptom = symptoms.get(symptom_alg_name, None)
		classifier = classifiers.get(classifier_name, None)

		return train_model(train, test, classifier(classlist, symptom), model_name)
	
	model_name = argv[1]
	return run_with_model(model_name)

	# classes = [line.strip() for line in open(CLASS_LIST_FILE).readlines()]

	# train_dialogs = load_zappe('train.txt', classes)
	# test_dialogs = load_zappe('test.txt', classes)

	# bayes = Bayes(classes, DocumentFrequency)
	# bayes.train(train_dialogs)


	# correct = 0

	# d = 0

	# for cls, sentences in test_dialogs.items():
	# 	expected = cls

	# 	for sentence in sentences:
	# 		d += 1
	# 		classified = bayes.classify(sentence)
	# 		if classified != expected:
	# 			print("incorrect match: ")
	# 			print(sentence)
	# 			print(f"matched as: {classified}, expected: {expected}")
	# 		else:
	# 			correct += 1

	# rate = correct / d

	# print(f"success rate: {rate}")

	# return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
