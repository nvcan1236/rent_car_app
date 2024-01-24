from app import admin, db
from flask_admin.contrib.sqla import ModelView
from app.models import Car, Color
from flask import session


class CarView(ModelView):
    column_list = ['name', 'seat_num', 'type', 'engine', 'price']


    def is_accessible(self):
        return session.get('login')


admin.add_view(CarView(Car, db.session))
