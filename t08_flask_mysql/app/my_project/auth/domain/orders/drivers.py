from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Driver(db.Model, IDto):
    """
    Model declaration for Driver with a one-to-many relationship to Cars.
    """
    __tablename__ = "drivers"

    driverID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    contact_number = db.Column(db.String(45))
    car_id = db.Column(db.Integer, db.ForeignKey('cars.carID'))
    car = db.relationship('Car', back_populates='drivers')

    # Relationship 1:M with DriverRatings
    driver_ratings = db.relationship('DriverRatings', back_populates='driver', cascade='all, delete-orphan')
    # Relationship 1:M with UserRatings
    user_ratings = db.relationship('UserRatings', back_populates='driver', cascade='all, delete-orphan')

    def __repr__(self) -> str:
        return (f"Driver({self.driverID}, '{self.first_name}', '{self.last_name}',"
                f" '{self.contact_number}', {self.car_id})")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship.
        :return: DTO object as dictionary
        """
        return {
            "driverID": self.driverID,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "contact_number": self.contact_number,
            "car_id": self.car_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Driver:
        """
        Creates domain object from DTO.
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Driver(
            first_name=dto_dict.get("first_name"),
            last_name=dto_dict.get("last_name"),
            contact_number=dto_dict.get("contact_number"),
            car_id=dto_dict.get("car_id")
        )
        return obj
