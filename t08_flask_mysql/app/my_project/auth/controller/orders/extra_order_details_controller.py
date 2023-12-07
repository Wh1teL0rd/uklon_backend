from t08_flask_mysql.app.my_project.auth.service import extra_order_details_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ExtraOrderDetailsController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = extra_order_details_service
