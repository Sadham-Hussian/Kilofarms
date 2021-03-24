from flask import Blueprint, render_template

blueprint = Blueprint('web', __name__, url_prefix='/web')


@blueprint.route('/login', methods=["GET"])
def web_login():
	return render_template('user/login.html')

@blueprint.route('/signup', methods=["GET"])
def web_signup():
	return render_template('user/signup.html')

@blueprint.route('/getAllProducts', methods=["GET"])
def web_product():
	return render_template('product/product.html')

@blueprint.route('/viewProduct/<int:product_id>', methods=["GET"])
def web_view_product(product_id):
	return render_template('product/view_product.html',product_id=product_id)