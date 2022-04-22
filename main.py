import json
from cls import Class
from dialog import Dialog
from bayes import Bayes
from symptom import bow, document_frequency, tfidf
import re


CLASS_LIST_FILE = 'DA_tridy.txt'


def load_train_dialogs(filename: str, classset: set[Class]):
	loaded_dialogs = []

	classdict = {item.name: item for item in classset}

	with open(filename) as file:
		data = json.load(file)
		for entry in data:
			if entry['error_code'] != 0:
				continue

			dialogs:list[str] = entry['dialog']

			for dialog in dialogs:
				sentences = dialog.split('>')
				for sentence in sentences:
					if sentence:
						pre, post = sentence.strip().split(' ', 1)
						cls, text = pre[1:], post
						text = re.sub(r'([,!\?\.\;\#\@\$\%\'\"]+|\-{2,})', '', text).strip()
						if text:
							loaded_dialogs.append(Dialog(text=text, cls=classdict[cls]))
		
	return loaded_dialogs

def load_zappe(filename: str, classset: set[Class]):
	loaded_dialogs = []
	classdict = {item.name: item for item in classset}

	with open(filename) as file:
		for line in file.readlines():
			line = line.split()
			cls = line[0]
			rest = " ".join(line[1:])
			loaded_dialogs.append(Dialog(text=rest, cls=classdict[cls]))
	
	return loaded_dialogs

def main():
	classset = {Class(line.strip()) for line in open('baba_tridy.txt').readlines()}
	# train_dialogs:list[Dialog] = load_train_dialogs('annotation.json', classset)

	train_dialogs = load_zappe('baba.txt', classset)
	# test_dialogs = load_zappe('test.txt', classset)

	bayes = Bayes(classset, document_frequency)
	bayes.train(train_dialogs)

	correct = 0


	for d in train_dialogs:
		classified = bayes.classify(d.text)
		expected = d.cls
		if classified != expected:
			print("incorrect match: ")
			print(d.text)
			print(f"matched as: {classified}, expected: {expected}")
		else:
			correct += 1

	rate = correct / len(train_dialogs)

	print(f"success rate: {rate}")
	
	# print(bayes.classify('it\'s hot outside'))

main()
