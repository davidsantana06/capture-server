from app.extensions import socket_io
from app.facades import response

from . import operations as error_operations


@socket_io.on_error_default
def handle_event_exception(e: Exception):
    code = error_operations.get_code(e)
    description = error_operations.get_description(code)
    return response.as_emission('error', description)
