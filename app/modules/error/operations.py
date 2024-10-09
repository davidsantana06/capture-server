from werkzeug.exceptions import HTTPException, InternalServerError


# common _

def get_code(e: Exception) -> int:
    is_http_exception = isinstance(e, HTTPException)
    return e.code if is_http_exception else InternalServerError.code


def get_description(code: int) -> str:
    return {
        404: 'The requested resource could not be found.',
        500: 'An unexpected error occurred on the server.',
    }.get(code, 'An error occurred. Please try again later.')
