from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class User(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "users"

    userID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    password = db.Column(db.String(45))
    current_location = db.Column(db.String(45))
    credit_card_number = db.Column(db.String(45))

    # Relationship 1:M

    def __repr__(self) -> str:
        return (f"User({self.userID}, '{self.first_name}', '{self.last_name}', '{self.email}',"
                f" '{self.password}', '{self.current_location}', '{self.credit_card_number}')")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "userID": self.userID,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "current_location": self.current_location,
            "credit_card_number": self.credit_card_number
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> User:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = User(
            first_name=dto_dict.get("first_name"),
            last_name=dto_dict.get("last_name"),
            email=dto_dict.get("email"),
            password=dto_dict.get("password"),
            current_location=dto_dict.get("current_location"),
            credit_card_number=dto_dict.get("credit_card_number")
        )
        return obj
