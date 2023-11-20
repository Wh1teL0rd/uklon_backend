from t08_flask_mysql.app.my_project.auth.service import user_ratings_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class UserRatingsController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = user_ratings_service
