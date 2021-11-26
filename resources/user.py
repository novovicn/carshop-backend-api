from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from models.user import UserModel
from werkzeug.security import safe_str_cmp

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists."}, 400
        
        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully"}, 201

class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        
        user = UserModel.find_by_username(data['username'])
        if user and safe_str_cmp(user.password, data['password']):
                access_token = create_access_token(identity=user.username)
                return {"token": access_token}
        return {'message': "Bad credentials."}
        
            