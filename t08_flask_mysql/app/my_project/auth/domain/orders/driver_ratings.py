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

    def __repr__(self) -> str:
        return f"DriverRatings({self.driver_ratings_id}, {self.rating}, {self.orders_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship.
        :return: DTO object as dictionary
        """
        return {
            "driver_ratings_id": self.driver_ratings_id,
            "rating": self.rating,
            "orders_id": self.orders_id
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
            orders_id=dto_dict.get("orders_id")
        )
        return obj