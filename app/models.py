from sqlalchemy import Column, String, Integer, Enum, Double, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from app import db, app
from enum import Enum as MyEnum


class SeatNum(MyEnum):
    XE_4_CHO = 4
    XE_5_CHO = 5
    XE_7_CHO = 7


class Type(MyEnum):
    SEDAN_4_CHO = 'Sedan 4 chổ'
    SUV_CUV_5_CHO = 'SUV & CUV 5 chổ'
    SUV_MPV_7_CHO = 'SUV & MPV 7 chổ'
    MERCEDES = 'Mercedes'


class Engine(MyEnum):
    TU_DONG = 'Tự động'
    SO_SAN = 'Số sàn'


class Car(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(100), nullable=False)
    seat_num = Column(Enum(SeatNum), default=SeatNum.XE_4_CHO)
    type = Column(Enum(Type), default=Type.SEDAN_4_CHO)
    engine = Column(Enum(Engine), default=Engine.TU_DONG)
    images = Column(String(800), default='')
    thumbnail = Column(String(200), default='')
    price = Column(Double, default=0)
    # colors = Column(ARRAY(Enum(Type)))
    # colors = relationship('Color', backref='car', lazy=True)


class Color(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(100), nullable=False)
    code = Column(String(20))


#
# class ColorCar(db.Model):
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     car_id = Column(Integer, ForeignKey(Car.id))
#     color = Column(Integer, ForeignKey(Color.id))

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
