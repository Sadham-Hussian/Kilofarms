
"""Settings configuration - Configuration for environment variables can goes here."""

from dotenv import load_dotenv

load_dotenv()

ENV = 'development'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:supersecret@localhost/kilofarms?host=localhost?port=3306'
SECRET_KEY = 'kilofarms'
SQLALCHEMY_TRACK_MODIFICATIONS = False