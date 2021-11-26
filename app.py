from flask import Flask 
from flask_restful import Api
from flask_jwt_extended import JWTManager, get_jwt_identity, create_access_token
from security import authenticate, identity
from resources.user import UserRegister, UserLogin
from resources.car import Car, Cars
from config import jwt_secret_key

from db import db

app = Flask(__name__)
db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = jwt_secret_key  
jwt = JWTManager(app)

api.add_resource(Car, '/cars/<string:id>')
api.add_resource(Cars, '/cars')

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/auth')
 
if __name__ == '__main__':
    app.run(port=5000)