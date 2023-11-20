from .orders.user_service import UserService
from .orders.car_service import CarService
from .orders.extra_order_details_service import ExtraOrderDetailsService

user_service = UserService()
car_service = CarService()
extra_order_details_service = ExtraOrderDetailsService()
