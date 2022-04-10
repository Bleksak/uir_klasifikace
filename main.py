import json
from cls import Class
from dialog import Dialog
from bayes import Bayes


CLASS_LIST_FILE = 'DA_tridy.txt'


def load_dialogs(filename: str, classset: set[Class]):
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
                        loaded_dialogs.append(Dialog(text=text, cls=classdict[cls]))
        
    return loaded_dialogs


def main():
    classset = {Class(line.strip()) for line in open(CLASS_LIST_FILE).readlines()}
    train_dialogs = load_dialogs('annotation.json', classset)

    bayes = Bayes(classset)
    bayes.train(train_dialogs)


main()
