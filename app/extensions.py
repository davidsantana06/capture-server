from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO


cors = CORS()
database = SQLAlchemy()
socket_io = SocketIO()
