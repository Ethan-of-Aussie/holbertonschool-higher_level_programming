#!/usr/bin/python3


from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

users = {
    "user1":
    {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1":
    {
        "username": "admin1",
         "password": generate_password_hash("password"),
         "role": "admin"
    }
}
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route('/basic-protected', methods=["GET"])
@auth.login_required
def index():
    return "Basic Auth: Access Granted"


@app.route('/login', methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username not in users or not check_password_hash(users[username]["password"], password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return  jsonify(access_token=access_token)


@app.route('/jwt-protected', methods=["GET"])
@jwt_required()
def jwtp():
    current_user = get_jwt_identity()
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=["GET"])
@jwt_required()
def adminonly():
    current_user = get_jwt_identity()
    if users[current_user]["role"] != "admin":
        return {"error": "Admin access required"}, 403
    return "Admin Access: Granted"

@jwt.unauthorized_loader
def missing_token_callback(err):
    return jsonify({"msg": "Missing authorization token"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(err):
    return jsonify({"msg": "Invalid token"}), 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"msg": "Token has expired"}), 401

@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({"msg": "Token has been revoked"}), 401

if __name__ == '__main__':
    app.run()
