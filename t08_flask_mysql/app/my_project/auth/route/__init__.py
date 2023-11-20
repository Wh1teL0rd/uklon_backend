from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.user_route import user_bp
    from .orders.car_route import car_bp
    from .orders.extra_order_details_route import extra_order_details_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(car_bp)
    app.register_blueprint(extra_order_details_bp)
