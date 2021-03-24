import json
import jwt
from flask import jsonify, make_response, request
from app.models.user import User
from app.extensions import db
from flask_bcrypt import check_password_hash, generate_password_hash
from datetime import datetime, timedelta
from functools import wraps
import app

def generate_jwt_token(username):
	token = jwt.encode({
    		'username': username,
    		'exp' : datetime.utcnow() + timedelta(days = 3)
    }, app.settings.SECRET_KEY)
	
	return token.decode('UTF-8')

def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None
		if 'Authorization' in request.headers:
			bearer, token = request.headers['Authorization'].split(" ")
		if not token:
			return make_response(jsonify({'error':'Token is missing!'}), 401)
		
		try:
			data = jwt.decode(token, app.settings.SECRET_KEY)
			current_user = User.query.filter_by(username=data['username']).first()
		except:
			return make_response(jsonify({'error':'Token is invalid!!'}), 401)

		return f(current_user, *args, **kwargs)
	return decorated


class Login():

	def __init__(self, params):
		self.username = params["username"]
		self.password = params["password"]

	def get(self):
		response = {"success":False}
		if self.username != "":
			user = User.query.filter_by(username=self.username).first()
			if user is not None and self.password != "":
				if check_password_hash(user.password, self.password):
					response["success"] = True
					response["token"] = generate_jwt_token(self.username)
					resp = make_response(jsonify(response), 200)
					resp.headers["Content-Type"] = "application/json"
					return resp
				else:
					response["error"] = "Incorrect password"
					return jsonify(response)
			else:
				response["error"] = "Invalid username"
				return jsonify(response)
		else:
			response["error"] = "Username needed"
			return jsonify(response)


class SignUp():

	def __init__(self, content):
		self.username = None
		self.password = None
		self.dob = None
		self.phone_number = None

		if 'username' in content:
			self.username = content['username']
		if 'password' in content:
			self.password = content['password']
		if 'dob' in content:
			self.dob = content['dob']
		if 'phone_number' in content:
			self.phone_number = content['phone_number']

	def post(self):
		response = {}
		response["success"] = False
		if self.username is not None and self.username != "":
			user = User.query.filter_by(username=self.username).first()
			if user is None:
				if self.password is not None and self.password != "":
					if self.dob is not None and self.dob != "":
						if self.phone_number is not None and self.phone_number != "":
							password_hash = generate_password_hash(self.password)
							user = User(self.username,password_hash,self.dob,self.phone_number)
							db.session.add(user)
							db.session.commit()
							response["success"] = True
							response["token"] = generate_jwt_token(self.username)
							resp = make_response(jsonify(response), 201)
							resp.headers["Content-Type"] = "application/json"
							return resp
						else:
							response["error"] = "Please enter phone_number"
							return jsonify(response)
					else:
						response["error"] = "Please enter dob"
						return jsonify(response)
				else:
					response["error"] = "Please enter password"
					return jsonify(response)
			else:
				response["error"] = "Username is already taken.."
				return jsonify(response)
		else:
			response["error"] = "Please enter username"
			return jsonify(response)
		return jsonify(response)