"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

api = Blueprint('api', __name__)


@api.route('/token', methods=['POST'])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    # if email != "test" or password != "test":
    #     return jsonify({"msg": "Bad username or password"}), 401
    user= User.query.filter_by(email=email).first()

    if not user: return jsonify({
        "messaje": "Usuario o contraseña incorrecto"
    })

    return jsonify({
        "messaje": "Usuario creado satisfactoriamente"
    })

    # access_token = create_access_token(identity=email)
    # return jsonify(access_token=access_token), 200



@api.route('/hello', methods=['GET'])
@jwt_required()
def get_hello(): 
    dictionary = {
            "message": "Hello World"
    }
    return jsonify(dictionary)



@api.route('/signup', methods=['POST'])
def signup():
    email = request.json.get("email")
    password = request.json.get("password")
    if not email or not password:
        return jsonify({"msg": "Email and password are required"}), 400

    # check if the user already exists in the database
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"msg": "User already exists"}), 409

    # create a new user
    new_user = User(email=email, password=password, is_active=True)
    db.session.add(new_user)
    db.session.commit()

    # generate an access token for the new user
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token), 200
