from flask import Blueprint, request, jsonify, make_response
from app.services.auth import token_required
from app.services.products import Product

blueprint = Blueprint('products', __name__, url_prefix='/products')

@blueprint.route('/createSKU', methods=["POST"])
@token_required
def create_product(current_user):
	content = request.get_json()
	product_service = Product(content, current_user.username)

	return product_service.post_create_product()

@blueprint.route('/product', methods=["GET", "PUT", "DELETE"])
@token_required
def view_product(current_user):
	if request.method == "GET":
		content = {}
		response = {}
		if "id" in request.args:
			content["id"] = request.args["id"]
		else:
			response["success"] = False
			response["error"] = "missing product id"
			return make_response(jsonify(response), 400)

		product_service = Product(content, current_user.username)

		return product_service.get_view_product()

	elif request.method == "PUT":
		content = {}
		response = {}
		if "id" in request.args:
			content["id"] = request.args["id"]
		else:
			response["success"] = False
			response["error"] = "missing product id"
			return make_response(jsonify(response), 400)
		
		req = request.get_json()
		flag = False
		if 'sku_name' in req:
			content["sku_name"] = req['sku_name']
			flag = True
		if 'sku_category' in req:
			content["sku_category"] = req['sku_category']
			flag = True
		if 'price' in req:
			content["price"] = req['price']
			flag = True

		if flag == False:
			response["success"] = False
			response["error"] = "no update data provided"
			return make_response(jsonify(response), 400)

		product_service = Product(content, current_user.username)

		return product_service.put_update_product()

	elif request.method == "DELETE":
		content = {}
		response = {}
		if "id" in request.args:
			content["id"] = request.args["id"]
		else:
			response["success"] = False
			response["error"] = "missing product id"
			return make_response(jsonify(response), 400)

		product_service = Product(content, current_user.username)

		return product_service.delete_product()

@blueprint.route("/getAllProducts", methods=["GET"])
@token_required
def get_all_products(current_user):
	content = {}

	product_service = Product(content, current_user.username)

	return product_service.get_all_products()