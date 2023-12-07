from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import extra_order_details_controller
from t08_flask_mysql.app.my_project.auth.domain import ExtraOrderDetails

extra_order_details_bp = Blueprint('extra_order_details', __name__, url_prefix='/extra-order-details')


@extra_order_details_bp.get('')
def get_all_extra_order_details() -> Response:
    """
    Gets all ExtraOrderDetails objects from the table using the Service layer.
    :return: Response object
    """
    return make_response(jsonify(extra_order_details_controller.find_all()), HTTPStatus.OK)


@extra_order_details_bp.post('')
def create_extra_order_details() -> Response:
    """
    Creates an ExtraOrderDetails object using the Service layer.
    :return: Response object
    """
    content = request.get_json()
    extra_order_details = ExtraOrderDetails.create_from_dto(content)
    extra_order_details_controller.create(extra_order_details)
    return make_response(jsonify(extra_order_details.put_into_dto()), HTTPStatus.CREATED)


@extra_order_details_bp.get('/<int:extra_order_details_id>')
def get_extra_order_details(extra_order_details_id: int) -> Response:
    """
    Gets ExtraOrderDetails by ID.
    :return: Response object
    """
    return make_response(jsonify(extra_order_details_controller.find_by_id(extra_order_details_id)), HTTPStatus.OK)


@extra_order_details_bp.put('/<int:extra_order_details_id>')
def update_extra_order_details(extra_order_details_id: int) -> Response:
    """
    Updates ExtraOrderDetails by ID.
    :return: Response object
    """
    content = request.get_json()
    extra_order_details = ExtraOrderDetails.create_from_dto(content)
    extra_order_details_controller.update(extra_order_details_id, extra_order_details)
    return make_response("ExtraOrderDetails updated", HTTPStatus.OK)


@extra_order_details_bp.patch('/<int:extra_order_details_id>')
def patch_extra_order_details(extra_order_details_id: int) -> Response:
    """
    Patches ExtraOrderDetails by ID.
    :return: Response object
    """
    content = request.get_json()
    extra_order_details_controller.patch(extra_order_details_id, content)
    return make_response("ExtraOrderDetails updated", HTTPStatus.OK)


@extra_order_details_bp.delete('/<int:extra_order_details_id>')
def delete_extra_order_details(extra_order_details_id: int) -> Response:
    """
    Deletes ExtraOrderDetails by ID.
    :return: Response object
    """
    extra_order_details_controller.delete(extra_order_details_id)
    return make_response("ExtraOrderDetails deleted", HTTPStatus.OK)
