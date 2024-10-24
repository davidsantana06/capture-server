from flask import Flask

from .config import setup_enviroment, setup_extensions
from .module.capture import capture
from .module.error import error


app = Flask(__name__)
setup_enviroment(app)
setup_extensions(app)
app.register_blueprint(capture)
app.register_blueprint(error)
