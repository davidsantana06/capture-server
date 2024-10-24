from app.extension import socket_io
from app.facade import response_facade

from . import capture_service, capture


# event _

@socket_io.on('print_screen')
def on_print_screen(base64: str):
    file_name = capture_service.generate_file_name()
    capture_service.store(base64, file_name)
    capture = capture_service.create(file_name)
    return response_facade.as_emission(
        'success',
        f'The capture was saved with identifier {capture.id}.'
    )


# route _

@capture.get('/all')
def get_all():
    captures = [c.to_dict() for c in capture_service.get_all()]
    return response_facade.as_json(captures)


@capture.get('/file/<int:id>')
def get_file_by_id(id: int):
    capture = capture_service.get_one_by_id(id)
    path = capture_service.compose_file_path(capture.file_name)
    return response_facade.as_file(path)
