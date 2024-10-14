from app.extensions import socket_io
from app.facades import response

from . import operations as capture_operations


@socket_io.on('print_screen')
def on_print_screen(base64: str):
    file_name = capture_operations.generate_file_name()
    capture_operations.store(base64, file_name)
    capture = capture_operations.create(file_name)
    return response.as_emission(
        'success',
        f'The capture was saved with identifier {capture.id}.'
    )
