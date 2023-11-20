from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Car(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "cars"

    carID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    car_type = db.Column(db.String(45))
    licence_plate = db.Column(db.String(45), unique=True)
    model = db.Column(db.String(45))
    year = db.Column(db.Integer)

    drivers = db.relationship('Driver', back_populates='car')

    def __repr__(self) -> str:
        return (f"Car({self.carID}, '{self.car_type}', '{self.licence_plate}', "
                f"'{self.model}', {self.year})")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "carID": self.carID,
            "car_type": self.car_type,
            "licence_plate": self.licence_plate,
            "model": self.model,
            "year": self.year
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Car:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Car(
            car_type=dto_dict.get("car_type"),
            licence_plate=dto_dict.get("licence_plate"),
            model=dto_dict.get("model"),
            year=dto_dict.get("year")
        )
        return obj
