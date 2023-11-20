from .orders.user_service import UserService
from .orders.car_service import CarService
from .orders.extra_order_details_service import ExtraOrderDetailsService
from .orders.driver_service import DriverService
from .orders.order_service import OrderService
from .orders.user_ratings_service import UserRatingService
from .orders.driver_ratings_service import DriverRatingService

user_service = UserService()
car_service = CarService()
extra_order_details_service = ExtraOrderDetailsService()
driver_service = DriverService()
order_service = OrderService()
user_ratings_service = UserRatingService()
driver_ratings_service = DriverRatingService()
