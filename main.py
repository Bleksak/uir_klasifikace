from cgi import test
import json
from document_frequency import DocumentFrequency
from bayes import Bayes
import re


CLASS_LIST_FILE = 'DA_tridy.txt'


# def load_train_dialogs(filename: str, classset: set[Class]):
# 	loaded_dialogs = []

# 	classdict = {item.name: item for item in classset}

# 	with open(filename) as file:
# 		data = json.load(file)
# 		for entry in data:
# 			if entry['error_code'] != 0:
# 				continue

# 			dialogs:list[str] = entry['dialog']

# 			for dialog in dialogs:
# 				sentences = dialog.split('>')
# 				for sentence in sentences:
# 					if sentence:
# 						pre, post = sentence.strip().split(' ', 1)
# 						cls, text = pre[1:], post
# 						text = re.sub(r'([,!\?\.\;\#\@\$\%\'\"]+|\-{2,})', '', text).strip()
# 						if text:
# 							loaded_dialogs.append(Dialog(text=text, cls=classdict[cls]))
		
	# return loaded_dialogs

def load_zappe(filename: str, classes: set[str]):
	loaded_dialogs = {cls: [] for cls in classes}

	with open(filename) as file:
		for line in file.readlines():
			line = line.split()
			cls = line[0]
			rest = " ".join(line[1:])
			loaded_dialogs[cls].append(rest)
	
	return loaded_dialogs

def main():
	classes = [line.strip() for line in open(CLASS_LIST_FILE).readlines()]

	train_dialogs = load_zappe('train.txt', classes)
	test_dialogs = load_zappe('test.txt', classes)

	bayes = Bayes(classes, DocumentFrequency)
	bayes.train(train_dialogs)

	# print(bayes.classify(test))

	correct = 0

	d = 0

	for cls, sentences in test_dialogs.items():
		expected = cls

		for sentence in sentences:
			d += 1
			classified = bayes.classify(sentence)
			if classified != expected:
				print("incorrect match: ")
				print(sentence)
				print(f"matched as: {classified}, expected: {expected}")
			else:
				correct += 1

	rate = correct / d

	print(f"success rate: {rate}")
	
	print(bayes.classify('go away'))

main()
