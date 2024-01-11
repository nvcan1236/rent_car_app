from sqlalchemy import Column, String, Integer
from app import db, app


class Car(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(100), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        car = Car(name='Vinfast')
        db.session.add(car)
        db.session.commit()
        db.create_all()
