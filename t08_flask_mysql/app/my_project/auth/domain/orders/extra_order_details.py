from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class ExtraOrderDetails(db.Model, IDto):
    """
    Model declaration for ExtraOrderDetails.
    """
    __tablename__ = "extra_order_details"

    idExtraOrderDetails = db.Column(db.Integer, primary_key=True, autoincrement=True)
    details = db.Column(db.String(255))
    ordersID = db.Column(db.Integer, db.ForeignKey('orders.ordersID'), unique=True, nullable=False)

    order = db.relationship('Order', back_populates='extra_order_details')

    def __repr__(self) -> str:
        return (f"ExtraOrderDetails({self.idExtraOrderDetails}, '{self.details}', "
                f"{self.ordersID})")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "idExtraOrderDetails": self.idExtraOrderDetails,
            "details": self.details,
            "ordersID": self.ordersID
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ExtraOrderDetails:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = ExtraOrderDetails(
            details=dto_dict.get("details"),
            ordersID=dto_dict.get("ordersID")
        )
        return obj
