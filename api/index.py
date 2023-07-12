from flask import Flask

app = Flask(__name__)
#Our sentences we like to encode

@app.route("/api/python")
def hello_world():
    return {
        "Test": "Test",
    }