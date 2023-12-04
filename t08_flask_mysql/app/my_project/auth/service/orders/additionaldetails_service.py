from t08_flask_mysql.app.my_project.auth.dao import additionaldetails_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class AdditionalDetailsService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = additionaldetails_dao
