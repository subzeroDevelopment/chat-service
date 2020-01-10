from flask import Flask,request,Response
from .utils import (validate_user_post,
                    save_user,get_users,
                    validate_users_send,
                    get_chat
                    )

app = Flask(__name__)

@app.route("/users",methods=['POST'])
def post_user():
    if not request.data:
        return {
            "message":"invalid json request"
        },400
    if not validate_user_post(request.json):
        return {
            "message":"invalid json body"
        },400
    if not save_user(request.json):
        return {
            "message":"the users already exists"
        },400
    return {
        "message":"ok"
    },200


@app.route("/users/<username>",methods=['GET'])
def get_contacts(username):
    data = get_users(username)
    print(data)
    return {
        "body":list(data),
    }

@app.route("/send",methods=['POST'])
def send_message():
    if not request.data:
        return {
            "message":"invalid json request"
        },400
    if not validate_users_send(request.json):
        return {
            "message":"invalid json body"
        },400
    chat_id = get_chat(request.json['users'])
    print(chat_id)
    return {
        "chat_id":chat_id
    }