from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import driver_ratings_controller
from t08_flask_mysql.app.my_project.auth.domain import DriverRatings

driver_ratings_bp = Blueprint('driver_ratings', __name__, url_prefix='/driver-ratings')


@driver_ratings_bp.get('')
def get_all_driver_ratings() -> Response:
    """
    Gets all Driver Ratings from the table using the Service layer.
    :return: Response object
    """
    return make_response(jsonify(driver_ratings_controller.find_all()), HTTPStatus.OK)


@driver_ratings_bp.post('')
def create_driver_rating() -> Response:
    """
    Creates a new Driver Rating.
    :return: Response object
    """
    content = request.get_json()
    driver_rating = DriverRatings.create_from_dto(content)
    driver_ratings_controller.create(driver_rating)
    return make_response(jsonify(driver_rating.put_into_dto()), HTTPStatus.CREATED)


@driver_ratings_bp.get('/<int:driver_ratings_id>')
def get_driver_rating(driver_ratings_id: int) -> Response:
    """
    Gets Driver Rating by ID.
    :return: Response object
    """
    return make_response(jsonify(driver_ratings_controller.find_by_id(driver_ratings_id)), HTTPStatus.OK)


@driver_ratings_bp.put('/<int:driver_ratings_id>')
def update_driver_rating(driver_ratings_id: int) -> Response:
    """
    Updates Driver Rating by ID.
    :return: Response object
    """
    content = request.get_json()
    driver_rating = DriverRatings.create_from_dto(content)
    driver_ratings_controller.update(driver_ratings_id, driver_rating)
    return make_response("Driver Rating updated", HTTPStatus.OK)


@driver_ratings_bp.patch('/<int:driver_ratings_id>')
def patch_driver_rating(driver_ratings_id: int) -> Response:
    """
    Patches Driver Rating by ID.
    :return: Response object
    """
    content = request.get_json()
    driver_ratings_controller.patch(driver_ratings_id, content)
    return make_response("Driver Rating updated", HTTPStatus.OK)


@driver_ratings_bp.delete('/<int:driver_ratings_id>')
def delete_driver_rating(driver_ratings_id: int) -> Response:
    """
    Deletes Driver Rating by ID.
    :return: Response object
    """
    driver_ratings_controller.delete(driver_ratings_id)
    return make_response("Driver Rating deleted", HTTPStatus.OK)
