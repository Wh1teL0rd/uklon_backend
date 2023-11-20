# orders DB
from .orders.user_dao import UserDAO
from .orders.car_dao import CarDAO
from .orders.extra_order_details_dao import ExtraOrderDetailsDAO

user_dao = UserDAO()
car_dao = CarDAO()
extra_order_details_dao = ExtraOrderDetailsDAO()
