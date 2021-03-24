from app.extensions import db

class Products(db.Model):
	__tablename__ = 'products'

	id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
	sku_name = db.Column(db.String(80), nullable=False)
	sku_category = db.Column(db.String(80), nullable=False)
	price = db.Column(db.Integer(), nullable=False)

	username = db.Column(db.String(80), db.ForeignKey('user.username'))

	def __init__(self, sku_name, sku_category, price, username):
		self.username = username
		self.sku_name = sku_name
		self.sku_category = sku_category
		self.price = price

	def serialize(self):
		return { 
			"id":self.id, 
			"sku_name":self.sku_name, 
			"sku_category":self.sku_category,
			"price":self.price,
			"username":self.username
		}