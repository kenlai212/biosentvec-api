import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
#import sent2vec

'''
model_path = "BioSentVec_PubMed_MIMICIII-bigram_d700.bin"
model = sent2vec.Sent2vecModel()
try:
    model.load_model(model_path)
except Exception as e:
    print(e)
'''

stop_words = set(stopwords.words('english'))
def preprocessSentence(text):
    text = text.replace('/',' / ')
    text = text.replace('.-',' .- ')
    text = text.replace('.',' . ')
    text = text.replace("\'"," \' ")
    text = text.lower()

    tokens = [token for token in word_tokenize(text) if token not in punctuation and token not in stop_words]
    return ' '.join(tokens)


def getVector(preppedSentence):
    #vector = model.embed_sentence(preppedSentence)
    #return vector
    return [0.001, 0.002, 0.003]


def validateGetVectorEmbedding(body):
    if body.get("sentence") is None:
        raise Exception("sentence is mandatory")