import util

sentence = input("Enter sentence for embedding : ")
preppedSentence = util.preprocessSentence(sentence)
vector = util.getVector(preppedSentence)

print("Original sentence : " + sentence)
print("Prepered sentence :" + preppedSentence)

vectorStr = ""
for i in vector:
    vectorStr += str(i) + ", "
print("Vector : " + vectorStr)