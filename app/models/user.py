from app.extensions import db
from app.models.products import Products

class User(db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.Text, nullable=False)
	dob = db.Column(db.Date, nullable=False)
	phone_number = db.Column(db.Unicode(20), nullable=False)

	product = db.relationship("Products")

	def __init__(self, username, password, dob, phone_number):
		self.username = username
		self.password = password
		self.dob = dob
		self.phone_number = phone_number
