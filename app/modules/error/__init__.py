from flask import Blueprint


error = Blueprint('error', __name__)


from .events import *
from .routes import *
