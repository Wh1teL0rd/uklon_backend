from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import DriverRatings
from typing import List


class DriverRatingsDAO(GeneralDAO):
    """
    Realisation of DriverRatings data access layer.
    """
    _domain_type = DriverRatings

    def find_by_rating(self, rating: int) -> List[object]:
        """
        Gets User Ratings objects from the database table by rating.
        :param rating: rating value
        :return: search objects
        """
        return self._session.query(DriverRatings).filter(DriverRatings.rating == rating).all()

    def find_by_orders_id(self, orders_id: int) -> List[object]:
        """
        Gets DriverRatings objects from the database table by orders_id.
        :param orders_id: ID value
        :return: Search objects
        """
        return self._session.query(DriverRatings).filter(DriverRatings.orders_id == orders_id).all()
