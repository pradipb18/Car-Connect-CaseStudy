from exception.exceptions import AuthenticationException
from dao.customer_service import CustomerService
from dao.admin_service import AdminService
from util.DBConnUtil import DBConnUtil

class AuthenticationService:
    def __init__(self, customer_service, db_conn_util,connection_string):
        self._customer_service = customer_service
        self._db_conn_util = db_conn_util
        self._connection_string = connection_string
    @staticmethod
    def authenticate_customer(username, password,connection_string):
        try:

            customer_service = CustomerService(DBConnUtil(), connection_string)

            customer_data = customer_service.GetCustomerByUsername(username)

            if customer_data and customer_data['Password'] == password:
                print("Authentication successful.")
                return customer_data
            else:
                raise AuthenticationException("Invalid customer credentials")

        except AuthenticationException as e:
            print(f"Error during customer authentication: {str(e)}")
            raise

    @staticmethod
    def authenticate_admin(username, password, connection_string):
        try:
            admin_service = AdminService(DBConnUtil(), connection_string)

            admin_data = admin_service.GetAdminByUsername(username)

            if admin_data and admin_data['Password'] == password:
                print("Authentication successful.")
                return admin_data
            else:
                raise AuthenticationException("Invalid admin credentials")

        except AuthenticationException as e:
            print(f"Error during admin authentication: {str(e)}")
            raise
