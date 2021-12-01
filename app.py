from flask import Flask 
from flask_restful import Api
from flask_jwt_extended import JWTManager, get_jwt_identity, create_access_token
from security import authenticate, identity
from resources.user import UserRegister, UserLogin, User
from resources.car import Car, Cars
from config import jwt_secret_key

from db import db

app = Flask(__name__)
db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = jwt_secret_key  
jwt = JWTManager(app)

@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:
        return {'is_admin': True}
    return {'is_admin' : False}



api.add_resource(Car, '/cars/<int:car_id>')
api.add_resource(Cars, '/cars')

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/auth')
api.add_resource(User, '/user/<int:user_id>')
 
if __name__ == '__main__':
    app.run(port=5000)