import logging
from flask.app import Flask
from apps.config.apps_config import db_session
import os

app = Flask(__name__)

from apps.billing.views import mod as billingModule
from apps.login.views import mod as loginModule
from apps.billing.views import init_scheduler

app.register_blueprint(billingModule)
app.register_blueprint(loginModule)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    db_session.close()


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()


init_scheduler()
'''
import sys, socket

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 47200))
except socket.error:
    print "!!!scheduler already started, DO NOTHING"
else:
    init_scheduler()
    print "scheduler started"


'''
