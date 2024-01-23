from app import app, db
from app.models import Car, Type
from flask import render_template, redirect
from app.admin import *


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/car-list')
def car_list():
    type1 = Car.query.filter(Car.type.__eq__(Type.SEDAN_4_CHO)).all()
    type2 = Car.query.filter(Car.type.__eq__(Type.SUV_CUV_5_CHO)).all()
    type3 = Car.query.filter(Car.type.__eq__(Type.SUV_MPV_7_CHO)).all()
    type4 = Car.query.filter(Car.type.__eq__(Type.MERCEDES)).all()
    return render_template('car-list.html',
                           type1=type1, type2=type2, type3=type3, type4=type4)


if __name__ == '__main__':
    app.run(debug=True)
