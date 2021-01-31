import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime, timedelta, date
from pytz import timezone
from time import strftime
from flask import Flask
from flask_cors import CORS
import sys
import os

# Import all the files where separate blueprints are created
from modules.web import web_app

# Setup for flask
app = Flask(__name__)
CORS(app)
app.debug = True
app.register_blueprint(web_app)
        

# For running project and logging
if __name__ == "__main__":
	handler_general = RotatingFileHandler('cargofl.log', maxBytes=10000, backupCount=10)
	datefmt = strftime("%a, %d %b %Y %H:%M:%S %p", datetime.now(timezone('Asia/Kolkata')).timetuple())
	formatter = logging.Formatter('%(levelname)s %(asctime)s %(funcName)s(),%(lineno)d %(message)s',datefmt=datefmt)
	handler_general.setFormatter(formatter)
	handler_general.setLevel(logging.DEBUG)
	# handler_general.setLevel(logging.INFO)
	# handler_general.setLevel(logging.WARNING)
	# handler_general.setLevel(logging.ERROR)
	# handler_general.setLevel(logging.CRITICAL)
	app.logger.addHandler(handler_general)
	app.run(port=5000)
