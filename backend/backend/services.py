from flask import Flask,request,Response
from .utils import validate_user_post,save_user

app = Flask(__name__)

@app.route("/user",methods=['POST'])
def home():
    if not request.data:
        return "invalid json request",400
    if not validate_user_post(request.json):
        return "invalid json body",400
    save_user(request.json)
    return "hola"