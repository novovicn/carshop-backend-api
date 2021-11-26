from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.car import CarModel

def add_arguments(parser):
    parser.add_argument('brand',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('model',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('year',
        type=int,
        required=True,
        help="Year must be between 1920 and 2022!"
    )
    parser.add_argument('image',
        type=str
    )
    parser.add_argument('mileage',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('vin',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('price',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )

class Car(Resource):
    parser = reqparse.RequestParser()
    add_arguments(parser)

    def get(self, _id):
        car = CarModel.find_by_id(_id)
        if car:
            return car.json()
        return {'message': 'Car not found'}, 404
    
    

    
class Cars(Resource):
    def get(self):
        return {'cars':[car.json() for car in CarModel.query.all()]}

    @jwt_required()
    def post(self):
        data = Car.parser.parse_args()
        car = CarModel(data['brand'], data['model'], data['year'], data['image'], data['mileage'], data['vin'], data['price'])
        try:
            car.save_to_db()
        except:
            return{"message": "An error occured saving a car."}
        
        return car.json(), 201