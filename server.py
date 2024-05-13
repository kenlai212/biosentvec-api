from flask import Flask, request, abort
import util as util

app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Welcome to Biosentvec-API</h2>'


@app.route('/sentence/vector-embedding', methods=['POST'])
def getVectorEmbedding():
    body = request.get_json()

    try:
        util.validateGetVectorEmbedding(body)
    except Exception as e:
        print(e)
        abort(400, e)
    
    try:
        preppedSentence = util.preprocessSentence(body["sentence"])
    except Exception as e:
         print(e)
         abort(500, "Cannot process sentence")

    try:    
        vector = util.getVector(preppedSentence)
    except Exception as e:
         print(e)
         abort(500, "Cannot get vector")

    return (vector)


if __name__ == "__main__":
    app.run(debug=True)