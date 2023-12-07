from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Driver
from typing import List


class DriverDAO(GeneralDAO):
    """
    Realization of Driver data access layer.
    """
    _domain_type = Driver

    def find_by_first_name(self, first_name: str) -> List[object]:
        """
        Gets Driver objects from the database table by the first name.
        :param first_name: first name value
        :return: search objects
        """
        return self._session.query(Driver).filter(Driver.first_name == first_name).order_by(Driver.first_name).all()

    def find_by_last_name(self, last_name: str) -> List[object]:
        """
        Gets Driver objects from the database table by the last name.
        :param last_name: last name value
        :return: search objects
        """
        return self._session.query(Driver).filter(Driver.last_name == last_name).order_by(
            Driver.last_name).all()

    def find_by_contact_number(self, contact_number: str) -> List[object]:
        """
        Gets Driver objects from the database table by contact number.
        :param contact_number: contact number value
        :return: search objects
        """
        return self._session.query(Driver).filter(Driver.contact_number == contact_number).order_by(
            Driver.contact_number).all()

    def find_by_car_id(self, car_id: int) -> List[object]:
        """
        Gets Driver objects from the database table by car ID.
        :param car_id: car ID value
        :return: search objects
        """
        return self._session.query(Driver).filter(Driver.car_id == car_id).order_by(Driver.car_id).all()
