from flask import Blueprint


capture = Blueprint('capture', __name__, url_prefix='/capture')


from .events import *
