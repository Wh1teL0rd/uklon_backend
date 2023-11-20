# orders DB
from .orders.user_dao import UserDAO
from .orders.car_dao import CarDAO
from .orders.extra_order_details_dao import ExtraOrderDetailsDAO
from .orders.driver_dao import DriverDAO
from .orders.order_dao import OrderDAO

user_dao = UserDAO()
car_dao = CarDAO()
extra_order_details_dao = ExtraOrderDetailsDAO()
driver_dao = DriverDAO()
order_dao = OrderDAO()
