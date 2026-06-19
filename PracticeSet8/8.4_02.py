import sys

def search_word(word, string):
    return string.count(word)

if __name__ == "__main__":
    file_name = sys.argv[1]
    word = sys.argv[2]
    with open(file_name, "r") as f:
        string = f.read()
        w = search_word(word, string)
    print(f"{w} times the {word} present in the file")
         