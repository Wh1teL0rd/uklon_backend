from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import UserRatings


class UserRatingsDAO(GeneralDAO):
    """
    Data access layer for User Ratings.
    """
    _domain_type = UserRatings

    def find_by_rating(self, rating: int) -> List[object]:
        """
        Gets User Ratings objects from the database table by rating.
        :param rating: rating value
        :return: search objects
        """
        return self._session.query(UserRatings).filter(UserRatings.rating == rating).all()

    def find_by_orders_id(self, orders_id: int) -> List[object]:
        """
        Gets User Ratings objects from the database table by orders_id.
        :param orders_id: orders_id value
        :return: search objects
        """
        return self._session.query(UserRatings).filter(UserRatings.orders_orders_id == orders_id).all()
