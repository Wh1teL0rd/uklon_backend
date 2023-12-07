from t08_flask_mysql.app.my_project.auth.dao import extra_order_details_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ExtraOrderDetailsService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = extra_order_details_dao
