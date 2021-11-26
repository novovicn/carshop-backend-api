from db import db 

class CarModel(db.Model):

    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(89))
    model = db.Column(db.String(89))
    year = db.Column(db.Integer)
    image = db.Column(db.String(500))
    mileage = db.Column(db.Integer)
    vin = db.Column(db.String(89))
    price = db.Column(db.Integer)

    def __init__(self, brand, model, year, image, mileage, vin, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.image = image
        self.mileage = mileage
        self.vin = vin
        self.price = price

    def json(self):
        return {'brand': self.brand, 'model': self.model, 'year': self.year, 'image': self.image, 'mileage': self.mileage, 'price': self.price, 'vin': self.vin}
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first() # SELECT * FROM items WHERE id=id LIMIT 1
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()