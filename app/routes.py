import app.util as util
from app import app
from flask import request, abort

@app.route('/')
@app.route('/index')
def index():
    return "Hello World"

@app.route('/sentence/vector-embedding', methods=['POST'])
def getVectorEmbedding():
    body = request.get_json()

    try:
        util.validateGetVectorEmbedding(body)
    except Exception as e:
        print(e)
        abort(400, e)
    
    try:
        sentence = util.preprocessSentence(body["sentence"])
    except Exception as e:
         print(e)
         abort(500, "Cannot process sentence")

    try:    
        vector = util.getVector(sentence)
    except Exception as e:
         print(e)
         abort(500, "Cannot get vector")

    return (vector)