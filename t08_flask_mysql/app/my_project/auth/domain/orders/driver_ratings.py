from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class DriverRatings(db.Model, IDto):
    """
    Model declaration for Driver Ratings.
    """
    __tablename__ = "driver_ratings"

    driver_ratings_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rating = db.Column(db.Integer)
    orders_id = db.Column(db.Integer, db.ForeignKey('orders.ordersID'))
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.driverID'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.userID'))

    # Relationship M:1 with User
    user = db.relationship('User', back_populates='driver_ratings')
    # Relationship M:1 із with Drivers
    driver = db.relationship('Driver', back_populates='driver_ratings')

    def __repr__(self) -> str:
        return (f"DriverRatings({self.driver_ratings_id}, {self.rating}, {self.orders_id}, "
                f"{self.driver_id}, {self.user_id})")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship.
        :return: DTO object as dictionary
        """
        return {
            "driver_ratings_id": self.driver_ratings_id,
            "rating": self.rating,
            "orders_id": self.orders_id,
            "driver_id": self.driver_id,
            "user_id": self.user_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> DriverRatings:
        """
        Creates domain object from DTO.
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = DriverRatings(
            rating=dto_dict.get("rating"),
            orders_id=dto_dict.get("orders_id"),
            driver_id=dto_dict.get("driver_id"),
            user_id=dto_dict.get("user_id")
        )
        return obj
