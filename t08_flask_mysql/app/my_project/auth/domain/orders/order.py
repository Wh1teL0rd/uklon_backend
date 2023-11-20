from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Order(db.Model, IDto):
    """
    Model declaration for Order Data Mapper.
    """
    __tablename__ = "orders"

    ordersID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.userID'))
    drivers_id = db.Column(db.Integer, db.ForeignKey('drivers.driverID'))
    car_id = db.Column(db.Integer, db.ForeignKey('cars.carID'))
    date = db.Column(db.DateTime)
    start_point = db.Column(db.String(45))
    end_point = db.Column(db.String(45))

    def __repr__(self) -> str:
        return (f"Order({self.ordersID}, {self.user_id}, {self.drivers_id}, {self.car_id}, '{self.date}', "
                f"'{self.start_point}', '{self.end_point}')")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "ordersID": self.ordersID,
            "user_id": self.user_id,
            "drivers_id": self.drivers_id,
            "car_id": self.car_id,
            "date": self.date.isoformat(),
            "start_point": self.start_point,
            "end_point": self.end_point
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Order:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Order(
            user_id=dto_dict.get("user_id"),
            drivers_id=dto_dict.get("drivers_id"),
            car_id=dto_dict.get("car_id"),
            date=dto_dict.get("date"),
            start_point=dto_dict.get("start_point"),
            end_point=dto_dict.get("end_point")
        )
        return obj
