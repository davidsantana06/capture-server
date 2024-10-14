from flask import (
    Response,
    jsonify, make_response, send_file
)
from flask_socketio import emit
from http import HTTPStatus
from pathlib import Path
from typing import Dict, List, Literal, Union


class ResponseFacade():
    def as_emission(
        self,
        event: Literal['success', 'error'],
        message: str,
    ) -> None:
        emit(event, message)

    def as_file(
        self,
        path: Path,
        status: HTTPStatus = HTTPStatus.OK
    ) -> Response:
        return make_response(
            send_file(path, as_attachment=True),
            status
        )

    def as_json(
        self,
        data: Union[Dict, List],
        status: HTTPStatus = HTTPStatus.OK
    ) -> Response:
        return make_response(
            jsonify(data),
            status
        )
