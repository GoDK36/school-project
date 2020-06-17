################################################################
################ Just Change this sections #####################
################################################################
# (1) Type Your Sentence

sent = "The professor permitted the students to take a nap during the class."
# (2) Make your CFG file for parsing your sentence.

# ex. grammar.cfg (see the direction in the powerpoint)

################################################################

import nltk
grammar = nltk.data.load(r"file:E:\Develop\python\school-project\컴언\NLTK\NLTK\cfg 파일\grammar5.cfg")
parser = nltk.ChartParser(grammar)
tokens = nltk.tokenize.word_tokenize(sent)
trees = parser.parse(tokens)

with open(r"E:\Develop\python\school-project\컴언\NLTK\result5.txt", "w") as f1:
    for tree in trees:
        print(tree)
        f1.write(str(tree)+"\n\n")
        tree.draw()

