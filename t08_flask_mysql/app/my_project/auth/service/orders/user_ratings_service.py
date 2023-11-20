from t08_flask_mysql.app.my_project.auth.dao import user_ratings_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class UserRatingService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = user_ratings_dao
