from http import HTTPStatus
from app.facades import response
from . import operations as error_operations, error


@error.app_errorhandler(Exception)
def handle_route_exception(e: Exception):
    code = error_operations.get_code(e)
    description = error_operations.get_description(code)
    return response.as_json(
        {'message': description},
        HTTPStatus(code)
    )
