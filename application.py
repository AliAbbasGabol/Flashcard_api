from flask import Flask, request

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "https://aliabbasgabol.github.io"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


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

