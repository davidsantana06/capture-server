from flask import Blueprint


capture = Blueprint('capture', __name__, url_prefix='/capture')


from . import service as capture_service
from .controller import *
