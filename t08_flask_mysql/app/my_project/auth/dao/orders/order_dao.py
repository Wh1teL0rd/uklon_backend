from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Order
from typing import List


class OrderDAO(GeneralDAO):
    """
    Realization of Order data access layer.
    """
    _domain_type = Order

    def find_by_user_id(self, user_id: int) -> List[object]:
        """
        Gets Order objects from the database table by user_id.
        :param user_id: user_id value
        :return: search objects
        """
        return self._session.query(Order).filter(Order.user_id == user_id).all()

    def find_by_drivers_id(self, drivers_id: int) -> List[object]:
        """
        Gets Order objects from the database table by drivers_id.
        :param drivers_id: drivers_id value
        :return: search objects
        """
        return self._session.query(Order).filter(Order.drivers_id == drivers_id).all()

    def find_by_car_id(self, car_id: int) -> List[object]:
        """
        Gets Order objects from the database table by car_id.
        :param car_id: car_id value
        :return: search objects
        """
        return self._session.query(Order).filter(Order.car_id == car_id).all()
