from sqlalchemy import func
from app import app, db
from app.models import Car, Type, SeatNum
from flask import render_template, redirect, request, session
from app.admin import *
from app.dao import check_user


@app.route('/admin/login', methods=['post'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    session['login'] = check_user(username=username, password=password)
    return redirect('/admin')


@app.route('/logout')
def logout():
    del session['login']
    return redirect('/admin')


@app.route('/')
def home():
    type1 = Car.query.filter(Car.type.__eq__(Type.SEDAN_4_CHO)).filter(Car.id.in_([5, 8, 10, 11])).all()
    type2 = Car.query.filter(Car.type.__eq__(Type.SUV_CUV_5_CHO)).filter(Car.id.in_([12, 13, 15, 35])).all()
    type3 = Car.query.filter(Car.type.__eq__(Type.SUV_MPV_7_CHO)).filter(Car.id.in_([17, 20, 27, 28])).all()
    type4 = Car.query.filter(Car.type.__eq__(Type.MERCEDES)).filter(Car.id.in_([29, 32, 36, 37])).all()
    car_id = request.args.get('car-id')
    if car_id:
        car_id = int(car_id)

    car = Car.query.get(car_id)

    return render_template('index.html',
                           type1=type1, type2=type2, type3=type3, type4=type4,
                           car=car)


@app.route('/car-list')
def car_list():
    type = request.args.get('type')
    kw = request.args.get('search')

    if kw:
        search = Car.query.filter(func.lower(Car.name).contains(kw.lower())).all()
        return render_template('car-list.html',
                               search=search, Type=Type, Seat=SeatNum, kw=kw)
    else:
        type1 = Car.query.filter(Car.type.__eq__(Type.SEDAN_4_CHO)).all()
        type2 = Car.query.filter(Car.type.__eq__(Type.SUV_CUV_5_CHO)).all()
        type3 = Car.query.filter(Car.type.__eq__(Type.SUV_MPV_7_CHO)).all()
        type4 = Car.query.filter(Car.type.__eq__(Type.MERCEDES)).all()

        if type == '1':
            return render_template('car-list.html',
                                   type1=type1, Type=Type, Seat=SeatNum, t=type1[0].type.value)
        elif type == '2':
            return render_template('car-list.html',
                                   type2=type2, Type=Type, Seat=SeatNum, t=type2[0].type.value)
        elif type == '3':
            return render_template('car-list.html',
                                   type3=type3, Type=Type, Seat=SeatNum, t=type3[0].type.value)
        elif type == '4':
            return render_template('car-list.html',
                                   type4=type4, Type=Type, Seat=SeatNum, t=type4[0].type.value)
        else:
            return render_template('car-list.html',
                                   type1=type1, type2=type2, type3=type3, type4=type4,
                                   Type=Type, Seat=SeatNum)


@app.route('/car-detail')
def car_detail():
    car_id = request.args.get('id')
    if car_id:
        car_id = int(car_id)

    car = Car.query.get(car_id)
    return render_template('car-detail.html', car=car)


if __name__ == '__main__':
    app.run(debug=True, port=5005)
