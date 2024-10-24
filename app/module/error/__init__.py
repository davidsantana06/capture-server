from flask import Blueprint


error = Blueprint('error', __name__)


from . import service as error_service
from .controller import *
