from app.facades import response
from . import operations as capture_operations, capture


@capture.get('/all')
def get_all():
    return response.as_json([
        c.to_dict() for c in
        capture_operations.get_all()
    ])


@capture.get('/file/<int:id>')
def get_file_by_id(id: int):
    capture = capture_operations.get_one_by_id(id)
    path = capture_operations.compose_file_path(
        capture.file_name
    )
    return response.as_file(path)
