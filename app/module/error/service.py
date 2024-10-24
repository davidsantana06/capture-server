from werkzeug.exceptions import HTTPException


# common _

def get_code(e: Exception) -> int:
    is_http_exception = isinstance(e, HTTPException)
    return e.code if is_http_exception else 500


def get_description(code: int) -> str:
    return {
        404: 'Resource not found.',
        500: 'Internal server error.',
    }.get(code, 'An unexpected error occurred.')
