from typing import List, Optional

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import AdditionalDetails


class AdditionalDetailsDAO(GeneralDAO):
    """
    Realization of AdditionalDetails data access layer.
    """
    _domain_type = AdditionalDetails

    def find_by_detail_info(self, detail_info: str) -> List[object]:
        """
        Gets AdditionalDetails objects from the database table by detail_info.
        :param detail_info: detail_info value
        :return: search objects
        """
        return self._session.query(AdditionalDetails).filter(AdditionalDetails.detail_info == detail_info).order_by(
            AdditionalDetails.detail_info).all()

    def find_by_car_id(self, carID: int) -> Optional[object]:
        """
        Gets AdditionalDetails object from the database table by carID.
        :param carID: carID value
        :return: search object or None if not found
        """
        return self._session.query(AdditionalDetails).filter(AdditionalDetails.carID == carID).first()

    def get_all_additional_details(self) -> List[object]:
        """
        Retrieve all AdditionalDetails records.
        :return: List of AdditionalDetails objects.
        """
        return self._session.query(AdditionalDetails).order_by(AdditionalDetails.detailID).all()

    def delete_additional_details(self, detailID: int) -> bool:
        """
        Delete AdditionalDetails by detailID.
        :param detailID: ID of the AdditionalDetails record to be deleted.
        :return: True if the record was successfully deleted, False otherwise.
        """
        additional_details_to_delete = self._session.query(AdditionalDetails).get(detailID)
        if additional_details_to_delete:
            self._session.delete(additional_details_to_delete)
            self._session.commit()
            return True
        return False
