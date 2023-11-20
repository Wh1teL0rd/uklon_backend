from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import user_ratings_controller
from t08_flask_mysql.app.my_project.auth.domain import UserRatings

user_ratings_bp = Blueprint('user_ratings', __name__, url_prefix='/user-ratings')


@user_ratings_bp.get('')
def get_all_user_ratings() -> Response:
    """
    Gets all User Ratings from the table using the Service layer.
    :return: Response object
    """
    return make_response(jsonify(user_ratings_controller.find_all()), HTTPStatus.OK)


@user_ratings_bp.post('')
def create_user_rating() -> Response:
    """
    Creates a new User Rating.
    :return: Response object
    """
    content = request.get_json()
    user_rating = UserRatings.create_from_dto(content)
    user_ratings_controller.create(user_rating)
    return make_response(jsonify(user_rating.put_into_dto()), HTTPStatus.CREATED)


@user_ratings_bp.get('/<int:user_ratings_id>')
def get_user_rating(user_ratings_id: int) -> Response:
    """
    Gets User Rating by ID.
    :return: Response object
    """
    return make_response(jsonify(user_ratings_controller.find_by_id(user_ratings_id)), HTTPStatus.OK)


@user_ratings_bp.put('/<int:user_ratings_id>')
def update_user_rating(user_ratings_id: int) -> Response:
    """
    Updates User Rating by ID.
    :return: Response object
    """
    content = request.get_json()
    user_rating = UserRatings.create_from_dto(content)
    user_ratings_controller.update(user_ratings_id, user_rating)
    return make_response("User Rating updated", HTTPStatus.OK)


@user_ratings_bp.patch('/<int:user_ratings_id>')
def patch_user_rating(user_ratings_id: int) -> Response:
    """
    Patches User Rating by ID.
    :return: Response object
    """
    content = request.get_json()
    user_ratings_controller.patch(user_ratings_id, content)
    return make_response("User Rating updated", HTTPStatus.OK)


@user_ratings_bp.delete('/<int:user_ratings_id>')
def delete_user_rating(user_ratings_id: int) -> Response:
    """
    Deletes User Rating by ID.
    :return: Response object
    """
    user_ratings_controller.delete(user_ratings_id)
    return make_response("User Rating deleted", HTTPStatus.OK)
