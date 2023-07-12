from flask import Flask
from sentence_transformers import SentenceTransformer

app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')

from sentence_transformers import SentenceTransformer
#Our sentences we like to encode
sentence = ['This framework generates embeddings for each input sentence']

#Sentences are encoded by calling model.encode()
embeddings = model.encode(sentence)


@app.route("/api/python")
def hello_world():
    return {
        "Test": "Test",
        "sentences": sentence,
        "embeddings": embeddings[0].tolist()
    }