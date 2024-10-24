from http import HTTPStatus

from app.extension import socket_io
from app.facade import response_facade

from . import error_service, error


# event _

@socket_io.on_error_default
def handle_event_exception(e: Exception):
    code = error_service.get_code(e)
    description = error_service.get_description(code)
    return response_facade.as_emission('error', description)


# route _

@error.app_errorhandler(Exception)
def handle_route_exception(e: Exception):
    code = error_service.get_code(e)
    description = error_service.get_description(code)
    return response_facade.as_json(
        {'message': description},
        HTTPStatus(code)
    )
