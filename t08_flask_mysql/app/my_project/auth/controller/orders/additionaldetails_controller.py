from t08_flask_mysql.app.my_project.auth.service import additionaldetails_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class AdditionalDetailsController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = additionaldetails_service
