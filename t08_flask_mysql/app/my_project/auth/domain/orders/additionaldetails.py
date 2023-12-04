from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class AdditionalDetails(db.Model, IDto):
    """
    Model declaration for AdditionalDetails.
    """
    __tablename__ = "additional_details"

    detailID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    detail_info = db.Column(db.String(255), nullable=False)
    carID = db.Column(db.Integer, db.ForeignKey('cars.carID'), nullable=False)

    # Define foreign key relationship
    car = db.relationship('Car', back_populates='additional_details')

    def __repr__(self) -> str:
        return f"AdditionalDetails({self.detailID}, '{self.detail_info}', {self.carID})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "detailID": self.detailID,
            "detail_info": self.detail_info,
            "carID": self.carID
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AdditionalDetails:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = AdditionalDetails(
            detail_info=dto_dict.get("detail_info"),
            carID=dto_dict.get("carID")
        )
        return obj
