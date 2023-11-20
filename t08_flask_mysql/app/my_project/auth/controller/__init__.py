from .orders.user_controller import UserController
from .orders.car_controller import CarController
from .orders.extra_order_details_controller import ExtraOrderDetailsController
from .orders.driver_controller import DriverController
from .orders.order_controller import OrderController
from .orders.user_ratings_controller import UserRatingsController
from .orders.driver_ratings_controller import DriverRatingsController

user_controller = UserController()
car_controller = CarController()
extra_order_details_controller = ExtraOrderDetailsController()
driver_controller = DriverController()
order_controller = OrderController()
user_ratings_controller = UserRatingsController()
driver_ratings_controller = DriverRatingsController()
