from flask import jsonify, make_response, request

from app.models.products import Products
from app.extensions import db

class Product():

	def __init__(self, content, username):
		self.username = username
		self.sku_name = None
		self.sku_category = None
		self.price = None
		self.id = None

		if 'sku_name' in content:
			self.sku_name = content['sku_name']
		if 'sku_category' in content:
			self.sku_category = content['sku_category']
		if 'price' in content:
			self.price = content['price']
		if 'id' in content:
			self.id = content['id']

	def post_create_product(self):
		response = {"success": False}
		if self.username and self.sku_name and self.sku_category and self.price:
			product = Products(self.sku_name,self.sku_category,self.price,self.username)
			db.session.add(product)
			db.session.commit()
			response["success"] = True
			response["id"] = product.id
			return make_response(jsonify(response), 201)
		else:
			response["error"] = "Invalid product data"
			return make_response(jsonify(response), 400)

	def is_product_belong_to_user(self):
		product = Products.query.filter_by(id=self.id,username=self.username).first()
		return product

	def get_view_product(self):
		response = {"success":False}
		if self.id and self.username:
			product = self.is_product_belong_to_user()
			if product is not None:
				response["success"] = True
				response["product"] = product.serialize()
				return make_response(jsonify(response), 200)
			else:
				response["error"] = "product not available for user"
				return make_response(jsonify(response), 401)
		else:
			response["error"] = "Invalid product id"
			return make_response(jsonify(response), 400)

	def put_update_product(self):
		response = {"success":False}
		if self.id and self.username:
			product = self.is_product_belong_to_user()
			if product is not None:
				if self.sku_name:
					product.sku_name = self.sku_name
				if self.sku_category:
					product.sku_category = self.sku_category
				if self.price:
					product.price = self.price
				db.session.commit()
				response["success"] = True
				response["product"] = product.serialize()
				return make_response(jsonify(response), 200)
			else:
				response["error"] = "product not available for user"
				return make_response(jsonify(response), 401)
		else:
			response["error"] = "Invalid product id"
			return make_response(jsonify(response), 400)

	def delete_product(self):
		response = {"success":False}
		if self.id and self.username:
			product = self.is_product_belong_to_user()
			if product is not None:
				db.session.delete(product)
				db.session.commit()
				response["success"] = True
				return make_response(jsonify(response), 202)
			else:
				response["error"] = "product not available for user"
				return make_response(jsonify(response), 401)
		else:
			response["error"] = "Invalid product id"
			return make_response(jsonify(response), 400)

	def get_all_products(self):
		response = {"success":False}
		if self.username:
			products = Products.query.all()
			result = []
			for product in products:
				result.append(product.serialize())
			response["products"] = result
			response["success"] = True
			return make_response(jsonify(response), 200)
		else:
			response["eror"] = "Invalid user"
			return make_response(jsonify(response), 400)
