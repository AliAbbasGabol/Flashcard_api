from flask import Flask, request
from supabase import create_client

supabase = create_client("https://yencscdknhajbandqzyy.supabase.co", "sb_publishable_QSJ-iEp8QEb1XHS6jkKtZA_rcDn_CUx")

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "https://aliabbasgabol.github.io"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


output = []

@app.route('/')
def index():
    return 'bonjour!'

@app.route("/Flashcards", methods= ["GET"])
def Outputer():
    response = supabase.table('FLash_Cards').select("*").execute()
    return response.data


@app.route("/Flashcards", methods= ["POST"])
def trnaslator():
    data = request.json
    response = supabase.table('FLash_Cards').insert(data).execute()
    return {
    "message": "Requested Flash card created sucessfully ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧, can be found on site✌️",
    "data": response.data
        }

@app.route("/Flashcards", methods= ["PUT"])
def updator():
    data = request.json
    response = supabase.table("FLash_Cards").update({"question": data['question'], "answer": data['answer']}).eq("id", data["id"]).execute()
    return {
        "message":"Requested data Updated sucessfully 🔄🔔🛠️",
        "data": response.data
        }

@app.route("/Flashcards", methods= ["DELETE"])
def deletor():
    data = request.json
    response = supabase.table("FLash_Cards").delete().eq("id", data['id']).execute()
    return { "meeesage": "🗑️ Requested data deleted sucessfully ( -_•)▄︻テحكـ━一💥�️",
    "data":response.data
    }