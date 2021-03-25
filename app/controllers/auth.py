from flask import Blueprint, request, jsonify, make_response, render_template

from app.services.auth import SignUp, Login, token_required

blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/login', methods=["GET"])
def login():
	"""
	This endpoint allows user to login. On successfull login 
	endpoint returns JWT token in the response else it returns 
	a error message.
	
	query parameters:
		username : username of the user
		password : password of the user
	"""
	
	params = {}
	response = {"success": False}
	if "username" in request.args:
		params["username"] = request.args["username"]
	else:
		response["error"] = "username needed"
		response["success"] = True
		return make_response(jsonify(response), 400)

	if "password" in request.args:
		params["password"] = request.args["password"]
	else:
		response["error"] = "password needed"
		return make_response(jsonify(response), 400)

	login_service = Login(params)

	return login_service.get()


@blueprint.route('/signup', methods=["POST"])
def signup():
	"""
	This endpoint allows user to signup. On successfull signup 
	endpoint returns JWT token in the response else it returns 
	a error message.
	
	request body:
		username : username of the user
		password : password of the user
		dob : dob of the user
		phone_number : mobile number 
	"""

	content = request.get_json()
	signup_service = SignUp(content)

	return signup_service.post()


@blueprint.route('/info', methods=["GET"])
@token_required
def user_info(current_user):
	"""
	This endpoint returns the details of the user
	from the JWT token in the Authorisation header. This 
	endpoint is for testing purpose.
	"""

	response = {}
	response["success"] = True
	response["username"] = current_user.username
	response["dob"] = current_user.dob
	response["phone_number"] = current_user.phone_number
	return make_response(jsonify(response), 200)
