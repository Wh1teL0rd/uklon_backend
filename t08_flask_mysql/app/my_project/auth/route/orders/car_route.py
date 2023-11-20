from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import car_controller
from t08_flask_mysql.app.my_project.auth.domain import Car

car_bp = Blueprint('cars', __name__, url_prefix='/cars')


@car_bp.get('')
def get_all_cars() -> Response:
    """
    Gets all objects from the table using the Service layer.
    :return: Response object
    """
    return make_response(jsonify(car_controller.find_all()), HTTPStatus.OK)


@car_bp.post('')
def create_car() -> Response:
    """
    Creates a new car.
    :return: Response object
    """
    content = request.get_json()
    car = Car.create_from_dto(content)
    car_controller.create(car)
    return make_response(jsonify(car.put_into_dto()), HTTPStatus.CREATED)


@car_bp.get('/<int:car_id>')
def get_car(car_id: int) -> Response:
    """
    Gets car by ID.
    :return: Response object
    """
    return make_response(jsonify(car_controller.find_by_id(car_id)), HTTPStatus.OK)


@car_bp.put('/<int:car_id>')
def update_car(car_id: int) -> Response:
    """
    Updates car by ID.
    :return: Response object
    """
    content = request.get_json()
    car = Car.create_from_dto(content)
    car_controller.update(car_id, car)
    return make_response("Car updated", HTTPStatus.OK)


@car_bp.patch('/<int:car_id>')
def patch_car(car_id: int) -> Response:
    """
    Patches car by ID.
    :return: Response object
    """
    content = request.get_json()
    car_controller.patch(car_id, content)
    return make_response("Car updated", HTTPStatus.OK)


@car_bp.delete('/<int:car_id>')
def delete_car(car_id: int) -> Response:
    """
    Deletes car by ID.
    :return: Response object
    """
    car_controller.delete(car_id)
    return make_response("Car deleted", HTTPStatus.OK)
