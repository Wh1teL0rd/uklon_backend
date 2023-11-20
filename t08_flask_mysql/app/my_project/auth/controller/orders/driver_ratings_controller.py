from t08_flask_mysql.app.my_project.auth.service import driver_ratings_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class DriverRatingsController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = driver_ratings_service
