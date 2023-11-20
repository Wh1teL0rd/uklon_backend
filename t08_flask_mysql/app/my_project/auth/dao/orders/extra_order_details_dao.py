from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import ExtraOrderDetails


class ExtraOrderDetailsDAO(GeneralDAO):
    """
    Realization of ExtraOrderDetails data access layer.
    """
    _domain_type = ExtraOrderDetails

    def find_by_details(self, details: str) -> List[object]:
        """
        Gets ExtraOrderDetails objects from the database table by details.
        :param details: Details value
        :return: Search objects
        """
        return self._session.query(ExtraOrderDetails).filter(ExtraOrderDetails.details == details).all()

    def find_by_orders_id(self, orders_id: int) -> List[object]:
        """
        Gets ExtraOrderDetails objects from the database table by Orders ID.
        :param orders_id: Orders ID value
        :return: Search objects
        """
        return self._session.query(ExtraOrderDetails).filter(ExtraOrderDetails.orders_id == orders_id).all()
