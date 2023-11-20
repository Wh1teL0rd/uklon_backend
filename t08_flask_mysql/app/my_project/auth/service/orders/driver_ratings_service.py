from t08_flask_mysql.app.my_project.auth.dao import driver_ratings_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class DriverRatingService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = driver_ratings_dao
