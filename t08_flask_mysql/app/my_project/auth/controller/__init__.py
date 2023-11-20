from .orders.user_controller import UserController
from .orders.car_controller import CarController
from .orders.extra_order_details_controller import ExtraOrderDetailsController
from .orders.driver_controller import DriverController
from .orders.order_controller import OrderController

user_controller = UserController()
car_controller = CarController()
extra_order_details_controller = ExtraOrderDetailsController()
driver_controller = DriverController()
order_controller = OrderController()
