import os.path

class Filereader:

    def __init__(self, name):
        if (os.path.exists(name) == True):
            self.filename = name
        else:
            raise FileExistsError("Error! File not found")

    def count_sentences(self):
        newtextfile = open(self.filename, "r")
        num_sentences = 0
        for line in newtextfile:
            sentencesinaline = line.split('.')
            num_sentences += len(sentencesinaline) - 1
        newtextfile.close()
        return num_sentences

    def count_words(self):
        newtextfile = open(self.filename, "r")
        num_words = 0
        for line in newtextfile:
            wordsinaline = line.split(' ')
            num_words += len(wordsinaline)
        newtextfile.close()
        return num_words

    def count_char(self):
        newtextfile = open(self.filename, "r")
        num_char = 0
        for line in newtextfile:
            wordsinaline = line.split(' ')
            num_char += sum(len(word) for word in wordsinaline)
        newtextfile.close()
        return num_char

if __name__ == '__main__':
    name = input("Enter your file name and directory: ")
    thisfile = Filereader(name)
    print(thisfile.count_sentences())
    print(thisfile.count_words())
    print(thisfile.count_char())