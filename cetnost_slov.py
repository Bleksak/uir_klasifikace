from operator import itemgetter
import sys

def count_words(text: str) -> tuple[str, int]:
    d: dict[str:int] = {}
    for word in map(lambda item: item.lower().strip('`.\'":'), text.split()):
        if word:
            d[word] = d.get(word, 0) + 1

    return sorted(d.items(), key=itemgetter(1))

def main():
    file = sys.argv[1] if len(sys.argv) >= 2 else None
    if not file:
        print("zadej soubor demente")
        return
    words = count_words(open(file).read())

    for key, value in words:
        print(f"{key:20s} => {value:3d}")

    print(f"soubor {file} obsahuje celkem {sum(map(itemgetter(1), words))} slov, z toho {len(words)} jedinecnych")

if __name__ == '__main__':
    main()