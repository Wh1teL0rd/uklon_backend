from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import additionaldetails_controller
from t08_flask_mysql.app.my_project.auth.domain import AdditionalDetails

additionaldetails_bp = Blueprint('additionaldetails', __name__, url_prefix='/additionaldetails')


@additionaldetails_bp.get('')
def get_all_additionaldetails() -> Response:
    """
    Gets all objects from the table using the Service layer.
    :return: Response object
    """
    return make_response(jsonify(additionaldetails_controller.find_all()), HTTPStatus.OK)


@additionaldetails_bp.post('')
def create_additionaldetails() -> Response:
    """
    Creates a new additional details record.
    :return: Response object
    """
    content = request.get_json()
    additionaldetails = AdditionalDetails.create_from_dto(content)
    additionaldetails_controller.create(additionaldetails)
    return make_response(jsonify(additionaldetails.put_into_dto()), HTTPStatus.CREATED)


@additionaldetails_bp.get('/<int:detail_id>')
def get_additionaldetails(detail_id: int) -> Response:
    """
    Gets additional details by ID.
    :return: Response object
    """
    return make_response(jsonify(additionaldetails_controller.find_by_id(detail_id)), HTTPStatus.OK)


@additionaldetails_bp.put('/<int:detail_id>')
def update_additionaldetails(detail_id: int) -> Response:
    """
    Updates additional details by ID.
    :return: Response object
    """
    content = request.get_json()
    additionaldetails = AdditionalDetails.create_from_dto(content)
    additionaldetails_controller.update(detail_id, additionaldetails)
    return make_response("AdditionalDetails updated", HTTPStatus.OK)


@additionaldetails_bp.patch('/<int:detail_id>')
def patch_additionaldetails(detail_id: int) -> Response:
    """
    Patches additional details by ID.
    :return: Response object
    """
    content = request.get_json()
    additionaldetails_controller.patch(detail_id, content)
    return make_response("AdditionalDetails updated", HTTPStatus.OK)


@additionaldetails_bp.delete('/<int:detail_id>')
def delete_additionaldetails(detail_id: int) -> Response:
    """
    Deletes additional details by ID.
    :return: Response object
    """
    additionaldetails_controller.delete(detail_id)
    return make_response("AdditionalDetails deleted", HTTPStatus.OK)
