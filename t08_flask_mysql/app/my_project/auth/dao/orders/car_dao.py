from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Car


class CarDAO(GeneralDAO):
    """
    Realization of Car data access layer.
    """
    _domain_type = Car

    def find_by_model(self, model: str) -> List[object]:
        """
        Gets Car objects from the database table by the model.
        :param model: model value
        :return: search objects
        """
        return self._session.query(Car).filter(Car.model == model).order_by(Car.model).all()

    def find_by_year(self, year: int) -> List[object]:
        """
        Gets Car objects from the database table by the year.
        :param year: year value
        :return: search objects
        """
        return self._session.query(Car).filter(Car.year == year).order_by(Car.year).all()

    def find_by_licence_plate(self, licence_plate: str) -> List[object]:
        """
        Gets Car objects from the database table by the licence_plate.
        :param licence_plate: licence_plate value
        :return: search objects
        """
        return self._session.query(Car).filter(Car.licence_plate == licence_plate).order_by(Car.licence_plate).all()

    def find_by_car_type(self, car_type: str) -> List[object]:
        """
        Gets Car objects from the database table by the car_type.
        :param car_type: car_type value
        :return: search objects
        """
        return self._session.query(Car).filter(Car.car_type == car_type).order_by(Car.car_type).all()
