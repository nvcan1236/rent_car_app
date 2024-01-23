from app import admin, db
from flask_admin.contrib.sqla import ModelView
from app.models import Car, Color


class CarView(ModelView):
    column_list = ['name', 'seat_num', 'type', 'engine', 'images', 'thumbnail', 'price']


admin.add_view(CarView(Car, db.session))
admin.add_view(ModelView(Color, db.session))
