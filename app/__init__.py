from flask import Flask

from .config import configure_enviroment, configure_extensions
from .modules.capture import capture, error


app = Flask(__name__)
configure_enviroment(app)
configure_extensions(app)
app.register_blueprint(capture)
app.register_blueprint(error)
