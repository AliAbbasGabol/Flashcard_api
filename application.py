from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
output = []

@app.route('/')
def index():
    return 'bonjour!'

@app.route("/Flashcards", methods= ["GET"])
def Outputer():
    return output


@app.route("/Flashcards", methods= ["POST"])
def trnaslator():
    Flashcard = {"question":request.json["question"], "answer":request.json["answer"]}
    output.append(Flashcard)
    print(output)
    return Flashcard

